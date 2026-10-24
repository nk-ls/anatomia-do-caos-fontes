# Anatomia do Caos — arquivo de fontes

Cópias datadas e verificáveis das fontes públicas usadas no levantamento
**Anatomia do Caos — a Covid-19 no Brasil em dados públicos**.

Links quebram, páginas mudam e matérias são editadas. Este repositório guarda, para cada fonte citada:

| Arquivo | O que é |
|---|---|
| `arquivo/<fonte>/<data>.html` ou `.pdf` | Cópia exatamente como baixada |
| `arquivo/<fonte>/<data>.txt` | Texto extraído, para leitura e busca |
| `arquivo/manifesto.csv` | URL, data e hora da coleta (UTC), status, tamanho, impressão digital SHA-256 e link da cópia no Internet Archive |

**Como conferir uma fonte:** abra o link original, a cópia do Internet Archive (coluna `wayback`) ou o arquivo aqui.
Para provar que a cópia não foi alterada, calcule o SHA-256 (`sha256sum arquivo.pdf`) e compare com o manifesto.

## Documentos oficiais

A pasta [`documentos/`](documentos/) guarda cópias integrais de documentos públicos: o **relatório final aprovado da CPI** (1.288 páginas), os **votos em separado** dos senadores contrários, o **contrato da Pfizer**, as **notas do Ministério da Saúde sobre a cloroquina** e outros, com impressão digital SHA-256.

## Como funciona

- A lista de fontes fica em [`lista/urls.txt`](lista/urls.txt).
- Uma rotina do GitHub Actions ([`coletar.yml`](.github/workflows/coletar.yml)) baixa cada link com
  [`scripts/coletar.py`](scripts/coletar.py) e salva aqui. Ela roda sempre que a lista muda.
- Nenhum dado pessoal privado é coletado: só páginas e documentos públicos.

## Documentário

A rotina [`transcrever.yml`](.github/workflows/transcrever.yml) obtém o texto falado do documentário
*Anatomia do Caos* (dir. Dandara Ferreira) para servir de roteiro de trabalho. Como a obra tem direitos
autorais, a transcrição completa é **guardada cifrada** (`transcricao/`) e não é publicada. O levantamento
usa só um roteiro resumido com minutagem e citações curtas.

## Licença

Scripts: MIT. As cópias das fontes pertencem aos seus autores e são guardadas apenas para fins de
verificação e citação.
