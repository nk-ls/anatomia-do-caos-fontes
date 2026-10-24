"""Obtém o texto falado de vídeos do YouTube (legenda publicada ou Whisper).

O resultado é CIFRADO antes de ir para o repositório público: obra audiovisual tem
direito autoral, e a transcrição completa serve só como material de trabalho.
Cifra híbrida: chave AES aleatória para o texto, e essa chave cifrada com a chave
pública em chave/transcricao_publica.pem. Só quem tem a chave privada abre.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def fmt(t: float) -> str:
    t = int(t)
    return f"{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}"


def via_api(vid: str):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi

        lista = YouTubeTranscriptApi().list(vid)
        for t in lista:
            print("legenda:", t.language_code, "gerada" if t.is_generated else "manual")
        dados = lista.find_transcript(["pt-BR", "pt", "pt-PT"]).fetch()
        return "legenda-youtube", [(s.start, s.text) for s in dados]
    except Exception as e:  # noqa: BLE001
        print("legenda indisponível:", repr(e)[:300])
        return None


def via_whisper(vid: str):
    tmp = Path("/tmp/audio")
    tmp.mkdir(exist_ok=True)
    r = subprocess.run(["yt-dlp", "-f", "bestaudio", "-x", "--audio-format", "mp3", "-o", str(tmp / f"{vid}.%(ext)s"),
                        f"https://www.youtube.com/watch?v={vid}"], capture_output=True, text=True)
    print(r.stdout[-800:], r.stderr[-800:])
    audio = next(tmp.glob(f"{vid}.*"), None)
    if not audio:
        return None
    from faster_whisper import WhisperModel

    segs, _ = WhisperModel("medium", device="cpu", compute_type="int8").transcribe(str(audio), language="pt", vad_filter=True)
    return "whisper-medium", [(s.start, s.text.strip()) for s in segs]


def cifrar(texto: str, destino: Path) -> None:
    destino.mkdir(parents=True, exist_ok=True)
    chave = os.urandom(32).hex()
    plano = Path("/tmp/plano.txt")
    plano.write_text(texto, encoding="utf-8")
    subprocess.run(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-salt", "-pass", f"pass:{chave}",
                    "-in", str(plano), "-out", str(destino / "texto.enc")], check=True)
    subprocess.run(["openssl", "pkeyutl", "-encrypt", "-pubin", "-inkey", str(RAIZ / "chave/transcricao_publica.pem"),
                    "-pkeyopt", "rsa_padding_mode:oaep", "-out", str(destino / "chave.enc")],
                   input=chave.encode(), check=True)
    plano.unlink()


def main() -> int:
    ok = False
    for vid in sys.argv[1:]:
        res = via_api(vid) or via_whisper(vid)
        if not res:
            print(f"FALHOU {vid}")
            continue
        metodo, trechos = res
        texto = f"# video {vid} | metodo: {metodo}\n" + "\n".join(f"[{fmt(t)}] {x}" for t, x in trechos)
        cifrar(texto, RAIZ / "transcricao" / vid)
        (RAIZ / "transcricao" / vid / "info.json").write_text(json.dumps({"video": vid, "metodo": metodo, "trechos": len(trechos)}))
        print(f"OK {vid}: {len(trechos)} trechos via {metodo}")
        ok = True
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
