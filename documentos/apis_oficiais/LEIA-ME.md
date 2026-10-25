
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
