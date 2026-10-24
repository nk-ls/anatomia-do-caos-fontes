// Coleta com navegador (Playwright/Chromium) as fontes que recusaram o coletor automático (scripts/coletar.py).
//
// Para cada URL de uma lista (um por linha), grava em arquivo/<id>/:
//   <data>.html  o HTML como o navegador montou a página (DOM renderizado), ou <data>.pdf se for PDF
//   <data>.txt   o texto visível da página (ou do PDF, via pdftotext), com URL, data e SHA-256 no topo
//   <data>.jpg   uma captura de tela da página (registro visual do que estava publicado)
// e acrescenta uma linha em arquivo/manifesto.csv com o SHA-256 do arquivo principal.
//
// Não contorna CAPTCHA, login nem bloqueio declarado: se a página for uma tela de verificação
// ("não sou um robô", "Just a moment", "Access denied"), a linha fica com status "bloqueado".
// Uso: NODE_PATH=$(npm root -g) node scripts/coletar_navegador.mjs lista.txt
// Varredura lenta: PAUSA_SEG=30 ESPERA_SEG=12 (pausa entre endereços e espera em cada página).
import { createRequire } from "node:module";
import { createHash } from "node:crypto";
import { readFileSync, writeFileSync, mkdirSync, appendFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const RAIZ = join(dirname(fileURLToPath(import.meta.url)), "..");
const ARQ = join(RAIZ, "arquivo");
const CAMPOS = ["id", "url", "coletado_em", "status", "url_final", "tipo", "bytes", "sha256", "texto_chars", "wayback", "erro"];
const PAUSA = Number(process.env.PAUSA_SEG || 0) * 1000;
const ESPERA = Number(process.env.ESPERA_SEG || 4) * 1000;
const BLOQUEIO = /(captcha|não sou um robô|i'?m not a robot|just a moment|attention required|access denied|acesso negado|verify you are human|cf-chl|checking your browser|request unsuccessful)/i;

// O mesmo identificador de scripts/coletar.py, para as duas coletas usarem as mesmas pastas.
function ident(url) {
  let base = url.replace(/^https?:\/\/(www\d*\.)?/, "").replace(/[^a-zA-Z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 90);
  return `${base}-${createHash("sha1").update(url).digest("hex").slice(0, 8)}`;
}
const sha = (b) => createHash("sha256").update(b).digest("hex");
const csv = (v) => (/[",\n]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : String(v));

const urls = readFileSync(process.argv[2], "utf8").split("\n").map((l) => l.trim()).filter((l) => l && !l.startsWith("#"));
const agora = new Date().toISOString().replace(/\.\d+Z$/, "Z");
const dia = agora.slice(0, 10);
// Se o ambiente usa proxy (variável HTTPS_PROXY), o navegador e os downloads passam por ele.
const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
const navegador = await chromium.launch(proxy ? { proxy: { server: proxy } } : {});
const contexto = await navegador.newContext({
  acceptDownloads: true, locale: "pt-BR", viewport: { width: 1280, height: 900 },
  userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
});

for (const url of urls) {
  const linha = Object.fromEntries(CAMPOS.map((c) => [c, ""]));
  Object.assign(linha, { id: ident(url), url, coletado_em: agora, erro: "coletado com navegador (Playwright); HTML renderizado" });
  const pasta = join(ARQ, linha.id);
  try {
    // PDFs: baixados direto pela sessão do navegador (mesmos cookies e cabeçalhos).
    const cab = await contexto.request.head(url, { timeout: 30000 }).catch(() => null);
    const tipoCab = cab?.headers()["content-type"] || "";
    if (/pdf/i.test(tipoCab) || /\.pdf($|\?)/i.test(url)) {
      const r = await contexto.request.get(url, { timeout: 90000 });
      let corpo = await r.body();
      linha.status = r.status(); linha.url_final = r.url();
      if (!(r.status() === 200 && corpo.subarray(0, 4).toString() === "%PDF")) {
        // 2ª tentativa: abrir o endereço no navegador, como um leitor, e guardar o download.
        const pagina = await contexto.newPage();
        try {
          const [baixado] = await Promise.all([
            pagina.waitForEvent("download", { timeout: 60000 }),
            pagina.goto(url, { timeout: 60000 }).catch(() => null),
          ]);
          corpo = readFileSync(await baixado.path());
          if (corpo.subarray(0, 4).toString() === "%PDF") { linha.status = 200; linha.url_final = baixado.url(); }
        } catch { /* sem download: segue com o status da 1ª tentativa */ }
        await pagina.close();
      }
      if (linha.status === 200 && corpo.subarray(0, 4).toString() === "%PDF") {
        mkdirSync(pasta, { recursive: true });
        const arq = join(pasta, `${dia}.pdf`);
        writeFileSync(arq, corpo);
        const texto = (() => { try { return execFileSync("pdftotext", ["-layout", arq, "-"]).toString(); } catch { return ""; } })();
        Object.assign(linha, { tipo: "pdf", bytes: corpo.length, sha256: sha(corpo), texto_chars: texto.length, erro: "coletado com navegador (Playwright)" });
        writeFileSync(join(pasta, `${dia}.txt`), `URL: ${url}\nColetado em: ${agora}\nSHA-256: ${linha.sha256}\n\n${texto}`);
      } else {
        if (linha.status === 200) linha.status = "bloqueado";
        linha.erro = "PDF não obtido (o site recusou ou devolveu tela de verificação); não contornado";
      }
    } else {
      const pagina = await contexto.newPage();
      const resp = await pagina.goto(url, { waitUntil: "domcontentloaded", timeout: 90000 });
      await pagina.waitForTimeout(ESPERA); // tempo para scripts da página e verificações automáticas (sem interação)
      const html = await pagina.content();
      const texto = await pagina.evaluate(() => document.body ? document.body.innerText : "");
      linha.status = resp ? resp.status() : ""; linha.url_final = pagina.url();
      if (linha.status !== 200 && texto.trim().length < 200) linha.erro = "o site recusou a página";
      if (BLOQUEIO.test(texto.slice(0, 3000)) || BLOQUEIO.test(await pagina.title()) || texto.trim().length < 200) {
        linha.status = "bloqueado"; linha.erro = "tela de verificação, bloqueio ou página vazia; não contornada";
      } else {
        mkdirSync(pasta, { recursive: true });
        const corpo = Buffer.from(html, "utf8");
        writeFileSync(join(pasta, `${dia}.html`), corpo);
        await pagina.screenshot({ path: join(pasta, `${dia}.jpg`), type: "jpeg", quality: 55, fullPage: false });
        Object.assign(linha, { status: 200, tipo: "text/html", bytes: corpo.length, sha256: sha(corpo), texto_chars: texto.length });
        writeFileSync(join(pasta, `${dia}.txt`), `URL: ${url}\nColetado em: ${agora}\nSHA-256: ${linha.sha256}\nMétodo: navegador (Playwright), HTML renderizado\n\n${texto}`);
      }
      await pagina.close();
    }
  } catch (e) {
    linha.erro = String(e.message || e).split("\n")[0].slice(0, 300);
  }
  appendFileSync(join(ARQ, "manifesto.csv"), CAMPOS.map((c) => csv(linha[c])).join(",") + "\n");
  console.log(linha.status || "ERRO", url, linha.status === 200 ? "" : linha.erro);
  if (PAUSA) await new Promise((r) => setTimeout(r, PAUSA));
}
await navegador.close();
