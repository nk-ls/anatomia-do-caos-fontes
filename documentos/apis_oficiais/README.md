# Respostas brutas de APIs oficiais

Guardadas byte a byte por `scripts/gerar_estados.py` do repositório principal, no momento em que o script gerou `dados/estados.csv` e `dados/pessoas_uf.csv`. Painel do Ministério da Saúde (óbitos e população por estado), API de dados abertos da Câmara e do Senado (estado do mandato).

| Arquivo | Origem | Coletado em |
|---|---|---|
| `camara_bia-kicis_leg57.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=Bia%20Kicis&idLegislatura=57 | 2026-10-24 |
| `camara_carla-zambelli_leg57.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=Carla%20Zambelli&idLegislatura=57 | 2026-10-24 |
| `camara_carlos-jordy_leg57.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=Carlos%20Jordy&idLegislatura=57 | 2026-10-24 |
| `camara_eduardo-bolsonaro_leg57.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=Eduardo%20Bolsonaro&idLegislatura=57 | 2026-10-24 |
| `camara_eduardo-pazuello_leg57.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=General%20Pazuello&idLegislatura=57 | 2026-10-24 |
| `camara_luis-miranda_leg56.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=Luis%20Miranda&idLegislatura=56 | 2026-10-24 |
| `camara_luis-miranda_leg57.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=Luis%20Miranda&idLegislatura=57 | 2026-10-24 |
| `camara_onyx-lorenzoni_leg56.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=Onyx%20Lorenzoni&idLegislatura=56 | 2026-10-24 |
| `camara_onyx-lorenzoni_leg57.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=Onyx%20Lorenzoni&idLegislatura=57 | 2026-10-24 |
| `camara_osmar-terra_leg57.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=Osmar%20Terra&idLegislatura=57 | 2026-10-24 |
| `camara_ricardo-barros_leg57.json` | https://dadosabertos.camara.leg.br/api/v2/deputados?nome=Ricardo%20Barros&idLegislatura=57 | 2026-10-24 |
| `ms_painel_PortalEstado.json` | https://qd28tcd6b5.execute-api.sa-east-1.amazonaws.com/prod/PortalEstado | 2026-10-24 |
| `senado_eduardo-braga.json` | https://legis.senado.leg.br/dadosabertos/senador/4994.json | 2026-10-24 |
| `senado_eduardo-girao.json` | https://legis.senado.leg.br/dadosabertos/senador/5976.json | 2026-10-24 |
| `senado_eduardo-girao_mandatos.json` | https://legis.senado.leg.br/dadosabertos/senador/5976/mandatos.json | 2026-10-24 |
| `senado_flavio-bolsonaro.json` | https://legis.senado.leg.br/dadosabertos/senador/5894.json | 2026-10-24 |
| `senado_humberto-costa.json` | https://legis.senado.leg.br/dadosabertos/senador/5008.json | 2026-10-24 |
| `senado_jorginho-mello.json` | https://legis.senado.leg.br/dadosabertos/senador/5350.json | 2026-10-24 |
| `senado_jorginho-mello_mandatos.json` | https://legis.senado.leg.br/dadosabertos/senador/5350/mandatos.json | 2026-10-24 |
| `senado_luis-carlos-heinze.json` | https://legis.senado.leg.br/dadosabertos/senador/1186.json | 2026-10-24 |
| `senado_marcos-rogerio.json` | https://legis.senado.leg.br/dadosabertos/senador/5422.json | 2026-10-24 |
| `senado_omar-aziz.json` | https://legis.senado.leg.br/dadosabertos/senador/5525.json | 2026-10-24 |
| `senado_otto-alencar.json` | https://legis.senado.leg.br/dadosabertos/senador/5523.json | 2026-10-24 |
| `senado_randolfe-rodrigues.json` | https://legis.senado.leg.br/dadosabertos/senador/5012.json | 2026-10-24 |
| `senado_renan-calheiros.json` | https://legis.senado.leg.br/dadosabertos/senador/70.json | 2026-10-24 |
| `senado_tasso-jereissati.json` | https://legis.senado.leg.br/dadosabertos/senador/3396.json | 2026-10-24 |
| `senado_tasso-jereissati_mandatos.json` | https://legis.senado.leg.br/dadosabertos/senador/3396/mandatos.json | 2026-10-24 |

## CNEP e CEIS — Portal da Transparência (CGU), 24/10/2026

Consulta à API oficial do Portal da Transparência, endpoints `/api-de-dados/cnep` e
`/api-de-dados/ceis`, filtrando por `codigoSancionado` (CNPJ). Um arquivo por empresa e
por base. Os de 2 bytes contêm `[]`: a empresa **não** tem registro naquela base, o que
também é informação.

| Arquivo | Empresa | CNPJ |
|---|---|---|
| `portaltransparencia_cnep_precisa_ovs_2026-10-24.json` | Precisa / OVS Importadora | 03.394.819/0001-79 |
| `portaltransparencia_ceis_precisa_ovs_2026-10-24.json` | idem | idem |
| `portaltransparencia_cnep_global_2026-10-24.json` | Global Gestão em Saúde | 10.375.666/0001-88 |
| `portaltransparencia_ceis_global_2026-10-24.json` | idem | idem |
| `portaltransparencia_cnep_vtclog_2026-10-24.json` | VTC Operadora Logística | 24.893.687/0001-08 |
| `portaltransparencia_ceis_vtclog_2026-10-24.json` | idem | idem |

**Cuidado ao reproduzir:** o parâmetro é `codigoSancionado`. Usar `cnpjSancionado` **não**
devolve erro — é silenciosamente ignorado, e a API responde a primeira página inteira de
sanções de empresas quaisquer. Conferir sempre se o CNPJ retornado é o pedido.
