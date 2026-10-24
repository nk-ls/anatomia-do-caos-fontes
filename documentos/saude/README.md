# OSINT: Saúde / Covid-19 no Brasil

Levantamento feito em 24/10/2026, só com fontes abertas. Os microdados com dados pessoais (SIVEP-Gripe/SRAG) foram lidos em fluxo (*streaming*) e agregados na hora. Nenhuma linha individual foi gravada em disco; só os agregados foram salvos.
Os arquivos citados estão nesta pasta.

## Tabela-resumo

| Item | Número/achado | Data de referência | Fonte (URL) | Oficial? | Arquivo |
|---|---|---|---|---|---|
| 1a. Óbitos acumulados (painel do MS, por data de notificação) | **715.295** no acumulado da SE 9/2025, que terminou em 01/03/2025. É o número que costuma ser citado como "11/03/2025". Para a data exata de divulgação de 11/03 não achei documento: o valor aparece na série semanal, entre 715.261 (SE 8) e 715.488 (SE 10) | SE 9/2025 | API do painel `https://qd28tcd6b5.execute-api.sa-east-1.amazonaws.com/prod/PortalCasos` (chamada pelo covid.saude.gov.br) | Sim (MS / Secretarias Estaduais) | [`painel_ms_api_PortalCasos_semanal.csv`](painel_ms_api_PortalCasos_semanal.csv), [`painel_ms_api_PortalCasos_raw_2026-10-24.json`](painel_ms_api_PortalCasos_raw_2026-10-24.json) |
| 1b. Número mais recente no painel | **716.626 óbitos** e **39.318.227 casos**. O último registro com movimento é a SE 35/2025 (30/08/2025; ano inferido porque 30/08 cai num sábado, fim de SE). Depois disso a série só tem zeros. Em 24/10/2026 o painel mostra "Atualizado em:" vazio e o endpoint `PortalGeral` responde 404. **Não achei número posterior a ago/set 2025** | 30/08/2025 | mesma API; print em [`painel_covid_screenshot.png`](painel_covid_screenshot.png) | Sim | idem |
| 1c. Óbitos por Covid em 2020 (painel, por notificação) | 195.725, o acumulado da SE 53/2020 | 2020 | mesma API | Sim | idem |
| 1d. Série mensal **por data de óbito**, 2020–2023 (SRAG hospitalizada) | 685.324 óbitos por SRAG-Covid com data entre 03/2020 e 12/2023: **2020: 207.754, 2021: 401.331, 2022: 65.509, 2023: 10.730**. Pico em **mar/2021, com 81.720**. Mais 2.019 óbitos sem data e 277 fora do intervalo. O SIVEP-Gripe pega só SRAG notificada, quase toda hospitalizada, por isso o total fica abaixo do total do painel | banco "vivo" de 23/03/2026 | `https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/20{20..23}/INFLUD{20..23}-23-03-2026.csv` (OpenDataSUS, conjunto `srag-2019-a-2026`) | Sim (microdado oficial, agregado por nós com CLASSI_FIN=5 e EVOLUCAO=2, mês de DT_EVOLUCA) | [`obitos_covid_srag_mes_obito_2020_2023.csv`](obitos_covid_srag_mes_obito_2020_2023.csv) |
| 2. Doses aplicadas por mês, 2021–2022 | **495,76 milhões de doses** de jan/2021 a dez/2022. Pico em **ago/2021, com 53,5 milhões**. Divididas em D1 177,4 mi, D2 162,1 mi, dose única 4,9 mi, reforço R 101,5 mi, R2 41,1 mi e as demais | aplicação 2021–2022 (*snapshot* do SI-PNI de 12/06/2023) | `https://github.com/covid19br/dados-vacinas` (pasta `doses_estados/`, gerada a partir dos microdados do SI-PNI/OpenDataSUS) | **Parcial**: a base é oficial (SI-PNI), mas a agregação é do Observatório Covid-19 BR. **Não consegui o agregado do próprio MS** | [`vacinacao_doses_mes_2021_2022.csv`](vacinacao_doses_mes_2021_2022.csv) |
| 3a. Ofício do MS à SEMSA Manaus sobre "tratamento precoce" | **Ofício nº 5/2021/SGTES/GAB/SGTES/MS**, de 07/01/2021, assinado por Mayra Pinheiro (SGTES). Pede autorização para difundir o tratamento precoce nas UBS. Chegou ao MPF (PGR/1ª CCR, procedimento 1.00.000.001030/2021-11) | 07/01/2021 (registro no DMPF-e de 16/03/2021) | https://transparencia.mpf.mp.br/conteudo/diarios-e-boletins/diario-eletronico-dmpf-e/2021/DMPF-EXTRAJUDICIAL-2021-03-16.pdf ; contexto: https://www.cnnbrasil.com.br/saude/2021/01/13/procurador-quer-investigacao-sobre-pedido-por-tratamento-precoce-em-manaus | Sim (MPF) para o número; íntegra do ofício **não localizada** | [`mpf_dmpf_extrajudicial_2021-03-16.pdf`](mpf_dmpf_extrajudicial_2021-03-16.pdf), [`mpf_dmpf_2021-03-16_trecho_oficio5_2021_SGTES.txt`](mpf_dmpf_2021-03-16_trecho_oficio5_2021_SGTES.txt) |
| 3b. Alerta da White Martins | O comunicado da White Martins à SES-AM é de **07/01/2021**. O MS ficou sabendo por e-mail de Petrônio Bastos (White Martins) em **08/01/2021**. O MS só começou a entregar oxigênio em **12/01/2021**. Tudo isso consta do Relatório Parcial de Ações do próprio MS, de 17/01/2021, citado pela PGR | 07–12/01/2021 | STF, INQ 4862 (decisão de abertura, rel. Lewandowski, assinada em 25/01/2021, com o ano escrito "2020" por erro de digitação): https://www.conjur.com.br/wp-content/uploads/2023/09/inq-4862.pdf | Sim (STF/PGR) | [`stf_inq4862_decisao_abertura_pazuello.pdf`](stf_inq4862_decisao_abertura_pazuello.pdf) |
| 3c. Ação do MPF/DPU sobre o oxigênio | ACP 1011497-89.2024.4.01.3200. Liminar de 17/06/2025 manda União, Amazonas e Manaus apurarem e coletarem dados. O MPF fala em "centenas de óbitos evitáveis". O pedido de indenização é de R$ 4 bi | 17/06/2025 | https://www.mpf.mp.br/o-mpf/unidades/pr-am/noticias/covid-19-justica-determina-medidas-de-reparacao-pelas-mortes-causadas-por-falta-de-oxigenio-em-manaus-am | Sim (MPF) | [`mpf_am_2025-06-17_acp_oxigenio.txt`](mpf_am_2025-06-17_acp_oxigenio.txt) |
| 3d. Mortes por falta de oxigênio | **33 a 34 mortes** em 14 e 15/01/2021 é o número "oficial inicial" segundo o procurador Igor Jordão Alves (MPF), em coletiva de 14/01/2026. O próprio MPF diz que esse número é subestimado: relatórios da ABIN apontam déficit de oxigênio de 28/12/2020 a 30/01/2021. O Simeam estimou 20–40 e depois ~60. **Não existe contagem oficial consolidada** | 14/01/2026 (coletiva) | https://vocativo.com/2026/01/14/crise-do-oxigenio-em-manaus-numero-de-vitimas-e-maior-que-imaginado/ ; https://amazoniareal.com.br/caos-na-pandemia-sem-oxigenio-pacientes-morrem-asfixiados-em-manaus/ | Não (imprensa relatando falas do MPF) | — |
| 4. Excesso de óbitos no Brasil, 2020–2022 | **1.135.580 óbitos em excesso por causas naturais**: 2020 = 299.324 (24%), 2021 = 552.282 (46%), 2022 = 283.974 (24%). Soma dos esperados: 3.647.654, o que dá 31% no período (cálculo nosso). Em 2023, só SE 1–12: 48.515 (18%) | painel atualizado em 18/07/2023 | Conass/CIEGES com Vital Strategies e Arpen-Brasil: https://cieges.conass.org.br/paineis/d6966d83-1709-4956-abb2-3d2ceb2b7b0d (dados lidos pela API Tableau do painel embutido, folhas "KPI Total", "KPI Total Esperado" e "KPI Total% Esperado" filtradas por `nu_ano`) | Semioficial (Conass é órgão colegiado dos secretários estaduais; base nos cartórios) | [`excesso_obitos_conass_vital_2020_2023.csv`](excesso_obitos_conass_vital_2020_2023.csv), [`excesso_conass_extracao_bruta.txt`](excesso_conass_extracao_bruta.txt), [`conass_excesso_screenshot.png`](conass_excesso_screenshot.png) |
| 4b. Excesso proporcional acumulado | BR **33,5%** de 15/03/2020 a 03/12/2022. AM tem o maior (63,4%) e RS o menor (23,8%) | 03/12/2022 | SEPLAG-RS com dados da Vital Strategies: https://planejamento.rs.gov.br/upload/arquivos/202302/17153053-excesso-de-obitos-rs-2023-02-15-1.pdf | Sim (governo do RS) | [`seplag_rs_vital_excesso_obitos_2023-02-15.pdf`](seplag_rs_vital_excesso_obitos_2023-02-15.pdf) |
| 4c. Para comparar: Fiocruz, só 2020 | Cerca de 190 mil óbitos em excesso (19%) em 2020 | 2020 | https://agenciabrasil.ebc.com.br/saude/noticia/2022-10/brasil-teve-190-mil-mortes-mais-em-2020-aponta-estudo-da-fiocruz | Acadêmico | — |
| 5. Órfãos da Covid | **149.000** crianças perderam pai, mãe ou os dois por Covid (IC95% 144–154 mil). Outras **135.000** perderam avô, avó ou outro parente cuidador que morava junto (85,9–199 mil). **149 + 135 = 284 mil.** Período 2020–2021. Por todas as causas: 1,3 milhão | publicado em 29/09/2025 (edição de nov/2025); repercutiu na imprensa em 27/10/2025 | Steyn N, Unwin HJT, … Hillis S, Barberia L, Souza AS, Castro MC, Flaxman S. *The Lancet Regional Health – Americas* 51:101252. **DOI 10.1016/j.lana.2025.101252**, PMID 41080610, PMCID PMC12513060. https://pubmed.ncbi.nlm.nih.gov/41080610/ ; preprint: medRxiv 10.1101/2025.01.31.25321479 | Acadêmico, revisado por pares (financiado por CDC/OMS) | [`orfaos_steyn2025_pubmed_abstract.txt`](orfaos_steyn2025_pubmed_abstract.txt) |

## Observações metodológicas

- **Total do painel e total do SRAG não são a mesma coisa.** O painel conta óbitos notificados pelas Secretarias Estaduais, pela data de notificação. O SRAG conta só os óbitos de SRAG notificada no SIVEP-Gripe, pela data do óbito. O "por data de óbito" pedido, para todos os óbitos, existe no SIM (CID U07.1/U07.2). Não consegui baixá-lo porque o TabNet e o FTP do DATASUS estão bloqueados aqui. O próximo passo seria o SIM do OpenDataSUS (`.../ckan.saude.gov.br/SIM/DO20OPEN.csv`); o bucket está acessível, mas o nome exato do arquivo atual não foi confirmado.
- **Linha SE 37 no CSV do painel:** "obitosNovos" = 517.480 é um artefato da janela móvel da API, que compara com a SE 53/2020. Não deve ser usado.
- **Filtro do SRAG:** CLASSI_FIN aparece como "5" ou "5.0" conforme o ano, e o script normaliza os dois. A data é DT_EVOLUCA (ISO). Script de agregação: `(área de trabalho da coleta)`.
- **Excesso de 2022 no Conass:** o total de óbitos esperados aparece idêntico ao de 2021 (1.208.317). Isso está no próprio painel e vale como ressalva.

## Não localizado

- Número oficial de óbitos por Covid posterior a ago/2025. O painel parou: "Atualizado em" vazio, `PortalGeral` 404 e série zerada depois de 30/08/2025.
- Arquivo `HIST_PAINEL_COVIDBR` atual. O botão "Arquivo CSV" depende do endpoint `PortalGeral`, que está quebrado.
- Documento de divulgação datado de 11/03/2025 com o número 715.295. O número existe na série (SE 9/2025), mas não achei o boletim ou release.
- Agregado oficial do MS de doses por mês (LocalizaSUS/vacinômetro e o Elasticsearch `imunizacao-es` retornaram 404).
- Íntegra do Ofício nº 5/2021/SGTES (só achei o registro no MPF e a cobertura de imprensa).
- Os ofícios da White Martins na íntegra (só achei a citação no Relatório Parcial do MS, via PGR/STF).
- Relatório da Polícia Federal sobre a crise do oxigênio (achei só reportagens sobre ele, como a do Metrópoles).
- Contagem oficial consolidada de mortes por asfixia em Manaus. Não existe; a ACP justamente pede a apuração.

## Domínios bloqueados ou fora do ar (deste ambiente, em 24/10/2026)

- `tabnet.datasus.gov.br`: DNS não resolve / conexão resetada.
- `ftp.datasus.gov.br`: conexão resetada.
- `dadosabertos.saude.gov.br` e `opendatasus.saude.gov.br` (CKAN/API): resposta vazia. O bucket S3 `ckan.saude.gov.br` funciona.
- `apidadosabertos.saude.gov.br`: resposta vazia.
- `xx9p7hp1p7.execute-api.us-east-1.amazonaws.com` (API antiga do painel): 502.
- `qsprod.saude.gov.br`: 502. `infoms.saude.gov.br` (painel de vacinação) e `imunizacao-es.saude.gov.br`: 404.
- `tableau.conass.org.br` pede login se acessado direto; só funciona embutido no CIEGES.
- `vocativo.com`: o WebFetch falhou com ENOTFOUND, mas o curl funcionou.
- `www.mpf.mp.br/pgr/documentos/PETINQPazuello92142021Recibo.pdf`: 404.


---
Cópias guardadas sem alteração; impressão digital de cada arquivo em [`SHA256SUMS`](SHA256SUMS) (`sha256sum -c SHA256SUMS`). As capturas de tela registram painéis dinâmicos (Conass e Ministério da Saúde) no dia da coleta.
