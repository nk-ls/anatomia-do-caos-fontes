"""Baixa cada URL de lista/urls.txt e guarda uma cópia datada em arquivo/.

Para cada fonte grava:
  arquivo/<id>/<data>.<ext>   cópia bruta (HTML ou PDF)
  arquivo/<id>/<data>.txt     texto extraído (trafilatura para HTML, pdftotext para PDF)
e acrescenta uma linha em arquivo/manifesto.csv com URL, data, status HTTP, URL final,
tipo, tamanho e SHA-256 da cópia bruta. Também pede uma cópia ao Internet Archive
(Wayback Machine) para que qualquer pessoa confira sem depender deste repositório.
"""
import csv
import hashlib
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx
import trafilatura

RAIZ = Path(__file__).resolve().parent.parent
ARQ = RAIZ / "arquivo"
MANIFESTO = ARQ / "manifesto.csv"
CAMPOS = ["id", "url", "coletado_em", "status", "url_final", "tipo", "bytes", "sha256", "texto_chars", "wayback", "erro"]
# User-Agent de navegador: portais .gov.br bloqueiam agentes que parecem robôs mesmo em páginas públicas.
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def ident(url: str) -> str:
    base = re.sub(r"^https?://(www\d*\.)?", "", url)
    base = re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-")[:90]
    return f"{base}-{hashlib.sha1(url.encode()).hexdigest()[:8]}"


def ja_coletadas() -> set[str]:
    if not MANIFESTO.exists():
        return set()
    with MANIFESTO.open(encoding="utf-8") as f:
        return {r["url"] for r in csv.DictReader(f) if r["status"] == "200"}


def wayback(cliente: httpx.Client, url: str) -> str:
    try:
        r = cliente.get(f"https://web.archive.org/save/{url}", timeout=120)
        loc = r.headers.get("content-location") or ""
        return f"https://web.archive.org{loc}" if loc.startswith("/web/") else str(r.url) if "/web/" in str(r.url) else ""
    except Exception:  # noqa: BLE001
        return ""


def coletar(cliente: httpx.Client, url: str, agora: str) -> dict:
    linha = dict.fromkeys(CAMPOS, "")
    linha.update(id=ident(url), url=url, coletado_em=agora)
    try:
        r = cliente.get(url, timeout=90)
        linha.update(status=r.status_code, url_final=str(r.url))
        tipo = r.headers.get("content-type", "").split(";")[0].strip()
        pdf = "pdf" in tipo or r.content[:4] == b"%PDF"
        linha["tipo"] = "pdf" if pdf else (tipo or "html")
        if r.status_code != 200:
            return linha
        if not pdf and "Verificação de segurança" in r.text:
            linha.update(status="bloqueado", erro="tela de verificação de segurança do site, não o documento")
            return linha
        pasta = ARQ / linha["id"]
        pasta.mkdir(parents=True, exist_ok=True)
        dia = agora[:10]
        bruto = pasta / f"{dia}.{'pdf' if pdf else 'html'}"
        if bruto.exists():  # nunca sobrescrever uma cópia já guardada: a nova ganha a hora no nome
            bruto = pasta / f"{dia}_{agora[11:19].replace(':', '')}.{'pdf' if pdf else 'html'}"
        bruto.write_bytes(r.content)
        linha.update(bytes=len(r.content), sha256=hashlib.sha256(r.content).hexdigest())
        if pdf:
            txt = subprocess.run(["pdftotext", "-layout", str(bruto), "-"], capture_output=True, text=True).stdout
        else:
            txt = trafilatura.extract(r.text, include_comments=False, include_tables=True, url=url) or ""
        bruto.with_suffix(".txt").write_text(f"URL: {url}\nColetado em: {agora}\nSHA-256: {linha['sha256']}\n\n{txt}", encoding="utf-8")
        linha["texto_chars"] = len(txt)
    except Exception as e:  # noqa: BLE001
        linha["erro"] = repr(e)[:300]
    return linha


def main() -> int:
    urls = [u.strip() for u in (RAIZ / "lista" / "urls.txt").read_text().splitlines() if u.strip() and not u.startswith("#")]
    feitas = ja_coletadas()
    novo = not MANIFESTO.exists()
    ARQ.mkdir(exist_ok=True)
    agora = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with httpx.Client(headers={"User-Agent": UA, "Accept-Language": "pt-BR,pt;q=0.9"}, follow_redirects=True) as cliente, \
            MANIFESTO.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if novo:
            w.writeheader()
        for url in urls:
            if url in feitas:
                continue
            linha = coletar(cliente, url, agora)
            if linha["status"] == 200 and "--sem-wayback" not in sys.argv:
                linha["wayback"] = wayback(cliente, url)
            w.writerow(linha)
            f.flush()
            print(linha["status"] or "ERRO", url, linha["erro"])
            time.sleep(1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
