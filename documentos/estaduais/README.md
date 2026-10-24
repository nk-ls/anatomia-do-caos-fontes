# Dinheiro público na pandemia: casos estaduais, municipais e de consórcio

Levantamento OSINT em fontes abertas. Coleta feita em **24/10/2026** (UTC). Os casos envolvem governos de partidos diferentes: PT/PSB e outros (Consórcio Nordeste), PSC (RJ e AM à época), MDB (PA e DF), PSL (SC à época), PSDB (SP) e PSB (Recife).

## Convenções

- **FATO**: está em documento oficial (STJ, STF, TCU, TCE, PF, MPF, TJ, Assembleia) ou no próprio texto da decisão.
- **ALEGAÇÃO**: acusação ou denúncia ainda não julgada no mérito, ou afirmação de parte interessada. **Ninguém é culpado sem condenação definitiva.**
- **DECISÃO**: ato decisório de tribunal, tribunal de contas ou tribunal de impeachment, com o estágio informado (provisória, recorrível ou definitiva).
- "Oficial?": **S** = documento oficial; **S-cópia** = texto oficial obtido em repositório de terceiro; **N (imprensa)** = cópia/imprensa, só como apoio.
- Pasta de evidências: esta pasta
  - Cada arquivo tem URL de origem, horário UTC da coleta, código HTTP e tamanho registrados em [`COLETA_LOG.tsv`](COLETA_LOG.tsv). As somas de verificação estão em `SHA256SUMS`.
  - Arquivos com `_imprensa` no nome são cópia de imprensa.
- **Limitações da coleta:**
  - As notícias antigas da PF e da CGU no gov.br agora pedem login. Pelo Wayback Machine (web.archive.org) a conexão caía neste ambiente. Esses links aparecem como "não baixado".
  - Do PF, só a tabela oficial de operações foi baixada.
  - O TCU e a página do Jusbrasil foram baixados com Playwright.
  - A busca de jurisprudência do STJ (scon) recusou a conexão.

---

## 1. Consórcio Nordeste: 300 respiradores da Hempcare

| Data | Tipo | O que diz | Valor | Fonte (URL) | Oficial? | Arquivo |
|---|---|---|---|---|---|---|
| 07–09/04/2020 | FATO | Dispensa 4/2020 e Contrato 5/2020 entre o Consórcio Nordeste e a Hempcare Pharma Representações Ltda. (CNPJ 34.049.323/0001-91) para 300 ventiladores. O pagamento foi integral e antecipado, ordenado em 08/04/2020 (OP 099001), sem garantia. | Contrato de **R$ 48.748.572,82** (empenho de R$ 48.748.575,82) | https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/886/2025/Plen%C3%A1rio | S | [`2025-04-23_TCU_Acordao_886-2025-Plenario_Consorcio_Nordeste_Hempcare.html`](2025-04-23_TCU_Acordao_886-2025-Plenario_Consorcio_Nordeste_Hempcare.html) |
| idem | FATO | Pela área técnica do TCU, só os aportes da Paraíba e de Sergipe tinham origem federal. | R$ 4.947.535,80 de cada estado, **R$ 9.895.071,60 federais** no total | idem | S | idem |
| 06/2020 | FATO (ato do Estado) | Operação Ragnarok, da Polícia Civil da BA. A PGE-BA diz que uma decisão judicial declarou a incompetência da Justiça estadual, os suspeitos foram soltos e a investigação parou. A PGE recorreu e acionou o CNJ e o CNMP. | — | https://www.ba.gov.br/pge/pge-ba-entra-com-medidas-administrativas-e-judiciais-para-garantir-prosseguimento-das-acoes-criminais | S (PGE-BA) | [`PGE-BA_medidas_prosseguimento_acoes_criminais_respiradores.html`](PGE-BA_medidas_prosseguimento_acoes_criminais_respiradores.html) |
| 06/2020 | FATO (imprensa) | O Consórcio entrou na Justiça para reaver o dinheiro. Foram bloqueadas 150 contas ligadas à empresa. O Ceará pôs R$ 5,4 mi (50 unidades). | R$ 48 mi cobrados | https://diariodonordeste.verdesmares.com.br/politica/consorcio-nordeste-aciona-justica-para-empresa-devolver-r-48-milhoes-1.2955167 | N (imprensa) | [`2020_DiarioNordeste_Consorcio_aciona_Justica_48mi_imprensa.html`](2020_DiarioNordeste_Consorcio_aciona_Justica_48mi_imprensa.html) |
| 05/2021 | DECISÃO administrativa (imprensa) | O Consórcio declarou a Hempcare inidônea, por até 2 anos ou até ressarcir (aviso no DOE-PI). | — | https://folhadomaranhao.com/2021/05/consorcio-nordeste-aplica-penalidade-a-hempcare-empresa-que-vendeu-respiradores-e-nao-entregou/ | N (imprensa) | [`2021-05_FolhaMaranhao_Consorcio_penalidade_Hempcare_imprensa.html`](2021-05_FolhaMaranhao_Consorcio_penalidade_Hempcare_imprensa.html) |
| 26/04/2022 | FATO | Operação Cianose (PF e CGU). O valor investigado é estelionato contra ente público, dispensa indevida e lavagem. | R$ 48,7 mi | https://www.gov.br/pf/pt-br/assuntos/noticias/2022/04/pf-investiga-irregularidades-em-contrato-de-compra-de-ventiladores-pulmonares e https://www.gov.br/cgu/pt-br/assuntos/noticias/2022/04/cgu-e-policia-federal-combatem-desvio-de-recursos-pelo-consorcio-nordeste | S | **não baixado** (gov.br pede login; Wayback inacessível) |
| 05/2022 | FATO (imprensa) | O RN recuperou parte da sua cota por ação própria. | **R$ 3.569.685,74** de R$ 4,9 mi | https://saibamais.jor.br/2022/05/rn-e-primeiro-estado-do-consorcio-nordeste-a-recuperar-dinheiro-de-compra-frustrada-de-respiradores/ | N (imprensa) | [`2022-05_SaibaMais_RN_recupera_dinheiro_respiradores_imprensa.html`](2022-05_SaibaMais_RN_recupera_dinheiro_respiradores_imprensa.html) |
| 08/2024 | FATO | 2ª fase da Cianose, com 34 mandados e sequestro de bens na BA, PR, RJ e SP (Justiça Federal da BA). | — | https://www.gov.br/pf/pt-br/assuntos/noticias/2024/08/pf-deflagra-operacao-para-recuperar-recursos-desviados-em-aquisicao-de-respiradores | S | **não baixado** |
| 23/04/2025 | DECISÃO (TCU) | **Acórdão 886/2025-Plenário** (TC 024.062/2020-0), placar de 5 a 3. O voto vencedor foi do ministro Bruno Dantas; o relator Jorge Oliveira ficou vencido, junto com Augusto Nardes e Jhonatan de Jesus. O TCU acolheu as justificativas de Carlos Gabas (secretário-executivo) e Valderir Claudino de Souza e converteu o processo em Tomada de Contas Especial **só contra a Hempcare**. A página do TCU avisa que os efeitos podem ter sido afetados pela decisão judicial **1059670-04.2025.4.01.3300/JFBA**. | TCE para quantificar o dano | URL TCU acima | S | [`2025-04-23_TCU_Acordao_886-2025-Plenario_Consorcio_Nordeste_Hempcare.html`](2025-04-23_TCU_Acordao_886-2025-Plenario_Consorcio_Nordeste_Hempcare.html) |
| idem | FATO (citado no acórdão) | O inquérito criminal consolidado no STJ é o **Inq 1426/DF**. O TCE-PB tinha proposta de condenar o governador **João Azevêdo** e o secretário de Saúde Geraldo Medeiros a ressarcir o Fundo Estadual de Saúde; a proposta aguardava parecer do MP de Contas. | — | idem | S | idem |
| 28/04/2025 | ALEGAÇÃO (imprensa, relatório da PF) | A PF afirma que o dinheiro saiu por transferências sucessivas para carros, imóveis e cartões. Pelo menos R$ 5 mi teriam ido para empresas sem vínculo com respiradores. Pela imprensa, em delação, a sócia Cristiana Taddeo admitiu comissões a lobistas. | — | https://pordentrodorn.com.br/2025/04/28/desvio-consorcio-nordeste-policia-federal-respiradores/ | N (imprensa) | [`2025-04-28_PorDentroRN_PF_aponta_uso_verba_respiradores_imprensa.html`](2025-04-28_PorDentroRN_PF_aponta_uso_verba_respiradores_imprensa.html) |
| 05/2025 e 05/2026 | FATO (imprensa) | A CGU abriu processos de responsabilização contra a Hempcare, a Gespar e outras empresas, e reconduziu as comissões por 180 dias em 05/2026. Um edital cobra R$ 14,1 mi atualizados de um dos alvos. | R$ 14,1 mi (parcial) | https://opotengi.com.br/cgu-mantem-processos-sobre-r-487-milhoes-pagos-por-respiradores-nao-entregues/ | N (imprensa) | [`2026-05_OPotengi_CGU_mantem_processos_Hempcare_imprensa.html`](2026-05_OPotengi_CGU_mantem_processos_Hempcare_imprensa.html) |
| 09/06/2026 | FATO (discurso) | O senador Girão (Novo-CE) cobrou a apuração no Plenário. O processo tem mais de mil páginas e "se arrasta" há seis anos. | — | https://www12.senado.leg.br/noticias/materias/2026/06/09/girao-cobra-apuracao-sobre-compra-de-respiradores-pelo-consorcio-nordeste | S (Agência Senado) | [`2026-06-09_Senado_noticia_Girao_Consorcio_Nordeste_respiradores.html`](2026-06-09_Senado_noticia_Girao_Consorcio_Nordeste_respiradores.html) |
| 07/2026 | DECISÃO (STF, imprensa) | O ministro Flávio Dino devolveu o inquérito ao STJ. Os fatos são de 2020, o mandato de governador terminou em 2022 e não há alegação de crime continuado no cargo de ministro. A PGR tinha pedido que o caso ficasse no STF. | — | https://jornaldebrasilia.com.br/noticias/politica-e-poder/flavio-dino-devolve-ao-stj-inquerito-sobre-desvios-na-compra-de-respiradores-por-rui-costa/ | N (imprensa) | [`2026-07_JornalDeBrasilia_Dino_devolve_STJ_inquerito_respiradores_imprensa.html`](2026-07_JornalDeBrasilia_Dino_devolve_STJ_inquerito_respiradores_imprensa.html) |
| 05–07/2026 | ALEGAÇÃO técnica (TCE-BA, imprensa) | Parecer da auditoria do TCE-BA sobre as contas de 2020: "erro grosseiro" de **Rui Costa** (que presidia o Consórcio) e de Carlos Gabas. Recomenda desaprovar as contas e manter a tentativa de recuperar o valor. **Ainda depende do plenário.** | R$ 48,7 mi | https://www.gazetadopovo.com.br/republica/auditoria-aponta-erro-grosseiro-de-rui-costa-no-caso-dos-respiradores/ | N (imprensa) | [`2026_GazetaDoPovo_auditoria_TCE-BA_erro_Rui_Costa_respiradores_imprensa.html`](2026_GazetaDoPovo_auditoria_TCE-BA_erro_Rui_Costa_respiradores_imprensa.html) |

**Situação atual (out/2026):**

- Inquérito criminal no STJ (Inq 1426/DF), **sem denúncia** contra gestores do Consórcio, até onde foi possível localizar.
- TCE no TCU contra a Hempcare, sem desfecho localizado.
- Processos da CGU contra empresas em andamento.
- Parecer do TCE-BA ainda não julgado.
- Ninguém foi condenado.

**Dinheiro:** R$ 48,7 mi pagos; R$ 3,57 mi recuperados pelo RN (imprensa). O total recuperado pelo Consórcio **não foi localizado**.

**Defesa:**

- Rui Costa nega irregularidade. Diz que foi ele quem mandou investigar e tentar recuperar o dinheiro, que havia emergência e escassez mundial e que não houve dolo nem erro grosseiro (imprensa).
- Gabas e Valderir tiveram as justificativas **acolhidas** pelo TCU.

---

## 2. Rio de Janeiro: Wilson Witzel (PSC), Iabas, hospitais de campanha e respiradores

| Data | Tipo | O que diz | Valor | Fonte (URL) | Oficial? | Arquivo |
|---|---|---|---|---|---|---|
| 26/05/2020 | FATO | Operação Placebo (PF), com 12 buscas no RJ e em SP, por "indícios de desvios de recursos públicos destinados ao atendimento de emergência". | Contratos investigados: **R$ 835.000.000,00** | https://www.gov.br/pf/pt-br/acesso-a-informacao/estatisticas/diretoria-de-investigacao-e-combate-ao-crime-organizado-dicor/operacoes-que-envolvam-investigacoes-de-recursos-federais-destinados-ao-combate-da-covid-19 | S | [`PF_tabela_operacoes_recursos_federais_COVID-19.html`](PF_tabela_operacoes_recursos_federais_COVID-19.html) (+ [`PF_tabela_operacoes_COVID_extraida_DERIVADO.tsv`](PF_tabela_operacoes_COVID_extraida_DERIVADO.tsv)) |
| 05/2020 | FATO (imprensa) | O TCE-RJ suspendeu pagamentos ao Iabas por suspeita de sobrepreço. Até 11/05/2020 o Iabas tinha recebido R$ 256 mi. A defesa do Iabas negou fraude. | R$ 256 mi pagos (até 11/05/2020) | https://www.cnnbrasil.com.br/nacional/tce-suspende-pagamento-a-organizacao-investigada-em-operacao-que-envolve-witzel/ | N (imprensa) | [`2020-05_CNN_TCE-RJ_suspende_pagamento_Iabas_imprensa.html`](2020-05_CNN_TCE-RJ_suspende_pagamento_Iabas_imprensa.html) |
| 28/08/2020 | DECISÃO (STJ, cautelar) | O ministro Benedito Gonçalves afastou Witzel por 180 dias (Operação Tris in Idem) e mandou prender preventivamente 6 pessoas (Mário Peixoto, Lucas Tristão e outros). O pedido de prisão de Witzel foi negado. | — | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/28082020-STJ-afasta-o-governador-Witzel-do-cargo-e-prende-seis-investigados-por-irregularidades-na-Saude-do-Rio.aspx | S | [`2020-08-28_STJ_afasta_Witzel_prende_seis_Tris_in_Idem.html`](2020-08-28_STJ_afasta_Witzel_prende_seis_Tris_in_Idem.html) |
| 28/08/2020 | FATO | Tris in Idem (PF/PGR): 6 prisões preventivas, 10 temporárias e 82 buscas. | — | URL da tabela PF acima | S | PF_tabela... |
| 02/09/2020 | DECISÃO (STJ) | A Corte Especial confirmou o afastamento por maioria; o ministro Napoleão Nunes Maia votou contra. | — | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/02092020-Corte-Especial-confirma-afastamento-do-governador-Wilson-Witzel-por-180-dias.aspx | S | [`2020-09-02_STJ_Corte_Especial_confirma_afastamento_Witzel_180dias.html`](2020-09-02_STJ_Corte_Especial_confirma_afastamento_Witzel_180dias.html) |
| 11/02/2021 | DECISÃO (STJ) | A Corte Especial recebeu por **unanimidade** a denúncia do MPF por **corrupção passiva majorada e lavagem**. Witzel virou **réu** e o afastamento foi prorrogado por 1 ano. Os demais investigados foram desmembrados. | — | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/11022021-Corte-Especial-recebe-denuncia-contra-Wilson-Witzel-por-corrupcao-passiva-e-lavagem-de-dinheiro.aspx | S | [`2021-02-11_STJ_noticia_Corte_Especial_recebe_denuncia_Witzel.html`](2021-02-11_STJ_noticia_Corte_Especial_recebe_denuncia_Witzel.html) |
| 17/03/2021 | DECISÃO (STJ) | Os autos de 8 investigados foram para a 7ª Vara Federal do RJ. | — | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/17032021-Corte-Especial-manda-a-Justica-Federal-investigacao-sobre-oito-pessoas-envolvidas-na-acao-contra-Witzel.aspx | S | [`2021-03-17_STJ_noticia_Corte_Especial_manda_Justica_Federal_8_pessoas_Witzel.html`](2021-03-17_STJ_noticia_Corte_Especial_manda_Justica_Federal_8_pessoas_Witzel.html) |
| 30/04/2021 | DECISÃO (impeachment) | O Tribunal Especial Misto (5 deputados e 5 desembargadores) aprovou o impeachment por **10 a 0**, com inabilitação por 5 anos. A acusação tratava das contratações das OSs Unir e Iabas; o contrato do Iabas era de R$ 835,8 mi para 7 hospitais (valor citado pela acusação). | R$ 835,8 mi (contrato Iabas) | https://agenciabrasil.ebc.com.br/politica/noticia/2021-04/tribunal-especial-aprova-impeachment-de-witzel | N (imprensa – Agência Brasil/EBC); confirmação oficial no item seguinte | [`2021-04-30_AgenciaBrasil_Tribunal_Especial_aprova_impeachment_Witzel_imprensa.html`](2021-04-30_AgenciaBrasil_Tribunal_Especial_aprova_impeachment_Witzel_imprensa.html) |
| 05/05/2021 | DECISÃO (STJ) | Notícia oficial que **confirma** a condenação de 30/04 pelo TEM (perda do cargo e 5 anos de inabilitação). O relator declarou a perda de competência do STJ e mandou os processos para a 7ª Vara Federal Criminal do RJ. | — | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/05052021-STJ-remete-para-Justica-Federal-do-Rio-processos-contra-Witzel-e-correus--.aspx | S | [`2021-05-05_STJ_remete_Justica_Federal_Rio_processos_Witzel.html`](2021-05-05_STJ_remete_Justica_Federal_Rio_processos_Witzel.html) |
| 16/06/2021 | DECISÃO (1ª instância) | A 7ª Vara Federal Criminal (juíza Caroline Figueiredo) recebeu denúncia do MPF por **organização criminosa** (desdobramento da Operação Favorito) contra Witzel, Helena Witzel e outras 8 pessoas. | — | https://agenciabrasil.ebc.com.br/geral/noticia/2021-06/ex-governador-do-rio-wilson-witzel-vira-reu-por-organizacao-criminosa | N (imprensa – EBC) | [`2021-06_AgenciaBrasil_Witzel_vira_reu_organizacao_criminosa_7VF_imprensa.html`](2021-06_AgenciaBrasil_Witzel_vira_reu_organizacao_criminosa_7VF_imprensa.html) |
| 30/03/2022 | DECISÃO (STJ) | O presidente do STJ negou a suspensão de segurança e manteve o impeachment; o mandado de segurança no TJRJ já tinha sido extinto. | — | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/30032022-STJ-nega-pedido-de-Witzel-para-voltar-ao-cargo-de-governador-do-Rio-de-Janeiro.aspx | S | [`2022-03-30_STJ_nega_retorno_Witzel_cargo.html`](2022-03-30_STJ_nega_retorno_Witzel_cargo.html) |
| 09/2025 | FATO (imprensa) | Com a nova tese do STF sobre foro (HC 232.627, de 2025), a ação penal **voltou ao STJ**. | — | https://platobr.com.br/com-processo-por-corrupcao-de-volta-ao-stj-witzel-aciona-stf-para-trancar-acao | N (imprensa) | [`2026-02_PlatoBR_Witzel_processo_volta_STJ_aciona_STF_imprensa.html`](2026-02_PlatoBR_Witzel_processo_volta_STJ_aciona_STF_imprensa.html) |
| 18/02/2026 | ALEGAÇÃO da defesa | Witzel pediu habeas corpus ao STF para trancar a ação (sob sigilo; distribuído a Nunes Marques). Diz que "nenhum dos contratos mencionados pelo MPF foi contestado pelo TCE, CGE, procuradoria do estado ou MP". | — | idem | N (imprensa) | idem |
| 13/05/2026 | DECISÃO (STJ, tese geral) | Tese da Corte Especial: o foro no STJ vale mesmo depois de a pessoa deixar o cargo e mesmo com a instrução encerrada na origem. A ação julgada **não é nomeada**, está sob sigilo. | — | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/13052026-Corte-Especial-decide-que-acao-penal-contra-ex-governador-deve-subir-para-o-STJ-mesmo-apos-fim-da-instrucao.aspx | S | [`2026-05-13_STJ_foro_especial_acao_penal_ex-governador_sobe_STJ.html`](2026-05-13_STJ_foro_especial_acao_penal_ex-governador_sobe_STJ.html) |

**Situação atual (out/2026):**

- **Impeachment:** definitivo (10 a 0, em 30/04/2021). A inabilitação de 5 anos venceu em 04/2026. Pela imprensa, Witzel desistiu de concorrer a governador em 08/2026.
- **Criminal:** ele é **réu**. A ação foi recebida no STJ em 2021, foi para a 7ª Vara Federal do RJ em 2021 e voltou ao STJ em 09/2025. **Não há sentença.** O resultado do habeas corpus no STF **não foi localizado**.
- A PlatôBR corrigiu a própria matéria a pedido de Witzel: segundo ele, a ação que está hoje no STJ trata de organização criminosa em contratos com OSs e com a Secretaria de Ciência e Tecnologia, e não diretamente de respiradores.

**Defesa:** Witzel sempre se declarou inocente. No impeachment, a defesa disse que as contratações foram decididas por secretários e subsecretários. Ele afirma que cancelou o contrato do Iabas quando soube das irregularidades.

---

## 3. Pará: Helder Barbalho (MDB), 400 respiradores da SKN (Operação Para Bellum)

| Data | Tipo | O que diz | Valor | Fonte (URL) | Oficial? | Arquivo |
|---|---|---|---|---|---|---|
| 13/05/2020 | FATO | Operação Profilaxia (PF/PA): "venda de respiradores inadequados". | R$ 25.200.000,00 | URL da tabela PF | S | [`PF_tabela_operacoes_recursos_federais_COVID-19.html`](PF_tabela_operacoes_recursos_federais_COVID-19.html) |
| 10/06/2020 | FATO | Operação **Para Bellum** (PF, autorizada pelo STJ): 23 buscas por fraude na compra de centenas de respiradores. Segunda fase em 23/06/2020, em Porto Alegre. | R$ 50.000.000,00 na tabela; a nota da PF fala em R$ 50,4 mi, metade antecipada | URL da tabela PF; nota: https://www.gov.br/pf/pt-br/assuntos/noticias/2020/06-noticias-de-junho-de-2020/policia-federal-deflagra-operacao-para-bellum-e-investiga-compra-de-respiradores-no-para | S | tabela baixada; a nota **não foi baixada** (gov.br pede login) |
| 06/2020 | DECISÃO cautelar (imprensa) | O ministro Francisco Falcão (STJ) bloqueou R$ 25 mi de Helder e de mais 7 pessoas. O governo disse que o sinal tinha sido devolvido e os aparelhos, devolvidos. | R$ 25 mi bloqueados; R$ 25,2 mi antecipados | https://istoe.com.br/stj-bloqueia-r-25-milhoes-de-helder-barbalho-e-mais-sete-investigados | N (imprensa) | não baixado |
| 03–04/10/2023 | DECISÃO (STJ) | **QO no Inq 1362/DF**, relator Falcão. Decisão monocrática de 03/10/2023, **referendada por unanimidade** pela Corte Especial em 04/10/2023: **arquivamento** em relação ao governador, a pedido da Vice-PGR. Pela PGR, havia tratativas pessoais de Helder com André Felipe de Oliveira da Silva (SKN), mas "não se depreende indicativo de que estava em curso um entendimento espúrio". A ressalva do art. 18 do CPP permite reabrir se houver prova nova. Os demais investigados foram para a 3ª Vara Federal de Belém. | — | https://www.jusbrasil.com.br/jurisprudencia/stj/2108108832/inteiro-teor-2108108833 | S-cópia (texto do acórdão no Jusbrasil) | [`STJ_QO_Inq1362_arquivamento_Helder_Barbalho_copia_JUSBRASIL.html`](STJ_QO_Inq1362_arquivamento_Helder_Barbalho_copia_JUSBRASIL.html) |
| 28/08/2025 | DECISÃO (1ª instância, imprensa) | A 3ª Vara Federal Criminal do PA recebeu a denúncia do MPF. Viraram **9 réus**, entre eles o ex-chefe da Casa Civil Parsifal Pontes, o ex-secretário de Saúde Alberto Beltrame, Peter Cassol Silveira, Leonardo Maia Nascimento e André Felipe de Oliveira da Silva (SKN). As acusações incluem fraude, peculato, corrupção e falsidade. O MPF pede o ressarcimento e dano moral coletivo. Helder **não** é réu. | MPF pede R$ 25,2 mi + R$ 500 mil por réu | https://revistacenarium.com.br/ex-secretarios-do-governo-do-para-viram-reus-por-fraude-em-respiradores-da-covid-19/ | N (imprensa) | [`2025-09_Cenarium_ex-secretarios_Para_viram_reus_respiradores_imprensa.html`](2025-09_Cenarium_ex-secretarios_Para_viram_reus_respiradores_imprensa.html) |

**Situação atual (out/2026):**

- **Helder Barbalho:** investigação **arquivada** pelo STJ (04/10/2023, unanimidade). Ele não é réu.
- **Ex-secretários e empresários:** réus desde 08/2025 na Justiça Federal do PA, **sem sentença**.

**Dinheiro:** R$ 50,4 mi contratados e R$ 25,2 mi antecipados. O governo do PA diz que o valor foi devolvido, mas **não há documento oficial localizado** que confirme o valor efetivamente recuperado.

**Defesa:** Helder sempre negou irregularidade.

---

## 4. Amazonas: Wilson Lima (PSC à época), respiradores comprados de loja de vinhos (Operação Sangria)

| Data | Tipo | O que diz | Valor | Fonte (URL) | Oficial? | Arquivo |
|---|---|---|---|---|---|---|
| 30/06/2020 | FATO | Operação **Sangria** (PF): fraude e superfaturamento em ventiladores; 8 prisões temporárias e 15 buscas. Fases 2 e 3 em 08/10/2020 e 30/11/2020. | Contrato de **R$ 2.976.000,00** | URL da tabela PF | S | [`PF_tabela_operacoes_recursos_federais_COVID-19.html`](PF_tabela_operacoes_recursos_federais_COVID-19.html) |
| 20/09/2021 | DECISÃO (STJ) | **APn 993**: a Corte Especial recebeu a denúncia por **unanimidade**. São réus Wilson Lima, o vice Carlos Alberto Filho (grafia da notícia do STJ) e mais 12 pessoas. Os crimes imputados são dispensa irregular, fraude, peculato, liderança de organização criminosa e embaraço. A denúncia contra Simone Papaiz e Flávio Cordeiro foi **rejeitada**. Pelo MPF: 28 respiradores, preço de mercado de cerca de R$ 17 mil contra mais de R$ 100 mil pagos, prejuízo acima de R$ 2 mi. | mais de R$ 2 mi de prejuízo (alegado) | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/20092021-Governador-do-Amazonas-vira-reu-no-STJ-por-fraude-na-compra-de-respiradores.aspx | S | [`2021-09-20_STJ_noticia_Wilson_Lima_vira_reu_respiradores.html`](2021-09-20_STJ_noticia_Wilson_Lima_vira_reu_respiradores.html); [`2021-11-03_STJ_APn993_acordao_recebimento_denuncia_Wilson_Lima.pdf`](2021-11-03_STJ_APn993_acordao_recebimento_denuncia_Wilson_Lima.pdf) |
| 05/2022 | DECISÃO (STJ) | Decisão monocrática na APn 993 (andamento processual). | — | https://processo.stj.jus.br/processo/dj/documento/?sequencial=154047603&num_registro=202000928826&data=20220520&data_pesquisa=20220520&tipo=0&formato=PDF&componente=MON | S | [`2022-05-20_STJ_APn993_decisao_monocratica.pdf`](2022-05-20_STJ_APn993_decisao_monocratica.pdf) |
| 06/02/2025 | DECISÃO (STJ) | **Rejeitada** outra denúncia, por peculato no frete aéreo dos respiradores, por falta de prova de dolo. O voto vencedor foi do ministro Raul Araújo; Falcão ficou vencido. A cadeia de preços descrita: a Sonoar comprou 28 aparelhos por R$ 1 mi e vendeu à FJAP (loja de vinhos) por R$ 2,4 mi, que revendeu ao Estado por R$ 2,9 mi. | Frete de R$ 191.852,80 | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2025/06022025-Rejeitada-denuncia-contra-governador-do-AM-por-peculato-em-transporte-de-respiradores-na-pandemia.aspx | S | [`2025-02-06_STJ_rejeita_denuncia_peculato_Wilson_Lima_transporte_respiradores.html`](2025-02-06_STJ_rejeita_denuncia_peculato_Wilson_Lima_transporte_respiradores.html) |
| 04/04/2026 | FATO (imprensa) | Wilson Lima renunciou ao governo para disputar o Senado. | — | https://www.moneytimes.com.br/wilson-lima-renuncia-como-governador-do-amazonas-e-cita-prazo-de-desincompatibilizacao/ | N (imprensa) | [`2026-04_MoneyTimes_Wilson_Lima_renuncia_governo_imprensa.html`](2026-04_MoneyTimes_Wilson_Lima_renuncia_governo_imprensa.html) |
| 02–08/09/2026 | DECISÃO em curso (imprensa) | Sessão virtual da Corte Especial sobre agravos regimentais de Lima e de Gutemberg Leão Alencar, que pediam tirar a relatoria de Nancy Andrighi (relatora desde 06/2026, depois que Falcão se declarou suspeito por foro íntimo). O relator dos agravos, Raul Araújo, votou contra. Placar parcial de **9 a 0 contra os recursos**. A discussão é processual. | — | https://ncnews.com.br/2026/09/06/stj-ja-tem-3-votos-contra-recursos-de-wilson-lima-na-operacao-sangria/ ; https://marioadolfo.com/stj-deve-concluir-hoje-julgamento-de-recurso-de-wilson-lima-sobre-compra-de-respiradores/ | N (imprensa) | 2026-09-06_NCNews_*; 2026-09_MarioAdolfo_*; 2026-09_Amazonas1_*; 2026-09_FatoAmazonico_* |

**Situação atual (out/2026):** Wilson Lima é **réu na APn 993 (STJ)**, sem julgamento de mérito. A proclamação oficial do resultado dos agravos **não foi localizada**; a imprensa dava 9 a 0 até 08/09/2026. Se os agravos forem rejeitados, o processo segue para a instrução.

**Defesa:** Wilson Lima nega as acusações e chama o caso de "fake news" (imprensa).

---

## 5. Santa Catarina: 200 respiradores da Veigamed e impeachment de Carlos Moisés (PSL à época)

| Data | Tipo | O que diz | Valor | Fonte (URL) | Oficial? | Arquivo |
|---|---|---|---|---|---|---|
| 26–27/03/2020 | FATO | Processo aberto na Secretaria de Saúde (SES) e dispensa aprovada no mesmo dia da proposta, com pagamento antecipado. O valor unitário foi de R$ 165 mil, contra o maior preço de mercado de R$ 72,6 mil (+137%). A SES anulou e rescindiu o contrato em 15/06/2020. | **R$ 33 mi pagos** | https://www.tcesc.tc.br/tcesc-determina-ressarcimento-de-valores-e-multa-aos-envolvidos-na-compra-irregular-de-200 | S | [`TCE-SC_determina_ressarcimento_multa_200_respiradores.html`](TCE-SC_determina_ressarcimento_multa_200_respiradores.html) |
| 30/09/2020 | FATO | Operação Pleumon (PF e MPF), com buscas inclusive na residência oficial do governador. | R$ 33.000.000,00 | URL da tabela PF | S | [`PF_tabela_operacoes_recursos_federais_COVID-19.html`](PF_tabela_operacoes_recursos_federais_COVID-19.html) |
| 07/05/2021 | DECISÃO (impeachment) | O Tribunal Especial **absolveu** Carlos Moisés por **6 a 4**; eram necessários 7 votos para condenar. Os 5 desembargadores e o deputado Laércio Schuster votaram pela condenação; os deputados Marcos Vieira, José Milton Scheffer, Valdir Cobalchini e Fabiano da Luz, pela absolvição. Ele estava afastado desde 30/03/2021 (denúncia recebida em 26/03/2021, também por 6 a 4). | — | https://www.alesc.sc.gov.br/agencia/noticia/moises-e-inocentado-no-caso-dos-respiradores-e-retornara-ao-comando-do-esta/ | S (Alesc) | [`2021-05-07_ALESC_Moises_absolvido_caso_respiradores.html`](2021-05-07_ALESC_Moises_absolvido_caso_respiradores.html); [`ALESC_retrospecto_impeachment_governador.html`](ALESC_retrospecto_impeachment_governador.html) |
| 04/09/2023 | DECISÃO (TCE-SC) | O Pleno julgou as contas **irregulares por unanimidade** (processo @TCE 20/00179260). Ressarcimento de R$ 33 mi pela Veigamed, Fábio Guasti, Pedro N. Araújo, Helton Zeferino, Douglas Borba, Márcia Pauli, José F. da Rocha, Carlos Charlie Maia e Carlos R. Costa Jr. Multa de R$ 19,9 mil para 5 deles. Depois houve recurso de reconsideração de Zeferino com efeito suspensivo parcial. | Ressarcimento de **R$ 33 mi** | URL TCE-SC acima; https://consulta.tce.sc.gov.br/Diario/dotc-e2023-11-13.pdf | S | TCE-SC_determina_*; [`2023-11-13_TCE-SC_Diario_Oficial_respiradores.pdf`](2023-11-13_TCE-SC_Diario_Oficial_respiradores.pdf) |
| 10/06/2025 | DECISÃO (criminal, 1ª instância) | O MPSC denunciou **14 pessoas**. A Vara Criminal da Região Metropolitana da Capital reconheceu a **prescrição** do peculato culposo para Zeferino, Charlie Maia e Costa Jr. Seguem as demais imputações. | — | https://www.tjsc.jus.br/web/imprensa/-/justica-reconhece-prescricao-punitiva-para-reus-no-caso-da-compra-dos-respiradores | S | [`TJSC_prescricao_punitiva_reus_compra_respiradores.html`](TJSC_prescricao_punitiva_reus_compra_respiradores.html) |
| ~10/07/2026 | DECISÃO (cível, 1ª instância, recorrível) | Sentença da 1ª Vara da Fazenda Pública da Capital (juíza Luciana P. Gottardi Trentini), na ação popular de Bruno Souza somada à ação do Estado. A Dispensa 754/2020 foi declarada **nula**. Veigamed, Rosemary N. de Araújo e Pedro N. Araújo devem devolver R$ 33 mi, descontado o que já foi recuperado ou bloqueado. Zeferino responde "na extensão de sua responsabilidade" (valor a apurar). A TS Eletronic também foi condenada. Moisés **não** era parte. | R$ 33 mi, mais dano moral coletivo (**valor divergente** na imprensa: R$ 19,8 mil ou R$ 19,8 mi; o texto fala em "60% do valor do contrato", o que corresponde a R$ 19,8 mi) | https://www.nsctotal.com.br/noticias/condenacao-de-ex-secretario-e-devolucao-de-r-33-milhoes-as-novas-decisoes-do-caso-dos-respiradores-em-sc ; https://ndmais.com.br/saude/caso-dos-respiradores-nova-sentenca-mantem-devolucao-de-r-33-milhoes-e-fixa-indenizacao-de-r-19-mil-aos-condenados-em-sc/ | N (imprensa); a sentença em si **não foi baixada** | 2026-07_NSC_*; 2026-07_NDmais_* |

**Situação atual (out/2026):**

- **Moisés:** absolvido no impeachment (definitivo). Não é réu nas ações citadas.
- **TCE-SC:** contas irregulares, com recurso de Zeferino.
- **Criminal:** ação penal com 14 denunciados em curso, com prescrição parcial.
- **Cível:** sentença de 07/2026, recorrível.

**Dinheiro:** R$ 33 mi pagos. O valor efetivamente recuperado **não foi localizado**; a sentença manda descontar o que já foi recuperado ou bloqueado.

**Defesa:**

- Zeferino diz que só autorizou a dispensa, com base em parecer jurídico. Atribui o pagamento antecipado a uma certificação falsa de notas fiscais e ao coordenador do Fundo Estadual de Saúde, e confia na improcedência.
- A Veigamed diz que tinha duas décadas de mercado e que o governo trocou o modelo pedido.

---

## 6. São Paulo: 3.000 respiradores chineses da Hichens Harrison (governo João Doria, PSDB)

| Data | Tipo | O que diz | Valor | Fonte (URL) | Oficial? | Arquivo |
|---|---|---|---|---|---|---|
| 04/2020 | FATO | Dispensa 50/2020 da SES-SP com a Hichens Harrison Capital Partner LLC. Empenhos de 14/04 e 23/04/2020. | **R$ 550.825.000,00** | https://www.tce.sp.gov.br/sites/default/files/noticias/20230830_Primeira%20C%C3%A2mara.pdf | S | [`2023-08-29_TCE-SP_Primeira_Camara_resultado_sessao.pdf`](2023-08-29_TCE-SP_Primeira_Camara_resultado_sessao.pdf) |
| 05/2020 | FATO | A presidência do TCE-SP mandou apurar a compra, a partir de representação do senador Major Olímpio. | — | https://www.tce.sp.gov.br/6524-tcesp-vai-apurar-compra-respiradores-pelo-governo-estadual | S | [`2020-05_TCE-SP_vai_apurar_compra_respiradores.html`](2020-05_TCE-SP_vai_apurar_compra_respiradores.html) |
| 06/2020 | ALEGAÇÃO (MP de Contas) | Representação do MPC-SP: a auditoria do TCE viu preços incompatíveis com o mercado e pediu apuração de dano. | — | https://www.mpc.sp.gov.br/sites/mpcsp/files/portal/2020/06/representacao._procedimento_10.040.20._respiradores._denuncia_senador_major_olimpio_5951-2365-3368-9502.pdf | S | [`2020-06_MPC-SP_representacao_respiradores_Major_Olimpio.pdf`](2020-06_MPC-SP_representacao_respiradores_Major_Olimpio.pdf) |
| 06/2020 | FATO (imprensa) | O governo cancelou a compra com cerca de 30% entregue e R$ 242 mi pagos antecipadamente. Depois, segundo o governo, 1.280 aparelhos foram entregues na repactuação, com a empresa amparada por liminar. | R$ 242 mi antecipados | https://www.cnnbrasil.com.br/nacional/mp-de-contas-apura-compra-de-respiradores-que-nao-foram-entregues-em-sp/ | N (imprensa) | não baixado |
| 19/02/2021 | FATO | Relatório final da CPI das Quarteirizações (Alesp), com capítulo sobre a compra. | — | https://www.al.sp.gov.br/repositorio/arquivoWeb/com/com6992.pdf | S (Diário da Alesp) | [`ALESP_CPI_relatorio_respiradores_com6992.pdf`](ALESP_CPI_relatorio_respiradores_com6992.pdf) |
| 29/08/2023 | DECISÃO (TCE-SP, 1ª Câmara, relator Antonio Roque Citadini) | TC-013441.989.20-9 (dispensa): **REGULAR**. TC-013562.989.20-2 (execução do contrato): **IRREGULAR**. TC-012647.989.20-1 (representação de Major Olímpio): **IMPROCEDENTE**. Cópia enviada ao MPF, ao MP estadual e ao Departamento de Polícia de Proteção à Cidadania. O próprio TCE avisa que o resultado é informativo, "sem efeitos legais" até a publicação no Diário Oficial. | — | URL TCE-SP acima | S | [`2023-08-29_TCE-SP_Primeira_Camara_resultado_sessao.pdf`](2023-08-29_TCE-SP_Primeira_Camara_resultado_sessao.pdf) |

**Situação atual:** o TCE-SP declarou a execução contratual irregular e a dispensa regular. **Não localizados:**

- recurso contra o acórdão;
- desfecho da ação de reparação do MP-SP;
- resultado da investigação da PF (citada na imprensa como "Operação Dragão", com sobrepreço de cerca de R$ 63 mi, que **não aparece na tabela oficial da PF**);
- valor recuperado.

**Defesa:** o governo Doria diz que a compra se justificou pela emergência, que a proposta foi a mais vantajosa e que os aparelhos acabaram entregues. Doria disse não temer a investigação (imprensa).

---

## 7. Outros casos com documento oficial

| Caso | Data | Tipo | O que diz | Valor | Fonte (URL) | Oficial? | Arquivo |
|---|---|---|---|---|---|---|---|
| **Recife/PE**, Operação Apneia (prefeitura, PSB) | 25/05/2020 (1ª fase) | FATO | Respiradores comprados por dispensa da microempresa Juvanete Barreto Freire (Brasmed Veterinária), com faturamento anual de R$ 81 mil. | Contratos de **R$ 11,5 mi** | https://www.mpf.mp.br/o-mpf/unidades/pr-pe/noticias/operacao-apneia-justica-federal-torna-reus-denunciados-pelo-mpf-por-irregularidades-na-compra-de-ventiladores | S | [`2025-02_MPF-PE_Operacao_Apneia_Justica_Federal_torna_reus.html`](2025-02_MPF-PE_Operacao_Apneia_Justica_Federal_torna_reus.html) |
| idem | 17/02/2025 | DECISÃO (recebimento) | Denúncia do MPF (de 2021) recebida contra **6 pessoas**, entre elas o ex-secretário de Saúde Jailson Correia, por contratação direta ilegal e peculato. O crime tributário prescreveu. Processo 0810085-30.2021.4.05.8300. **Sem sentença localizada.** A prefeitura diz que devolveu os aparelhos por falta de certificação da Anvisa (imprensa). | — | idem | S | idem |
| **Distrito Federal**, Operação Falso Negativo (governo Ibaneis, MDB) | 25/08/2020 | ALEGAÇÃO (MPDFT) | Prisão do secretário de Saúde Francisco Araújo e de outros gestores por fraude na compra de testes de Covid. | MPDFT estima R$ 46 mi de dano (R$ 18 mi em testes) | https://www.metropoles.com/distrito-federal/falso-negativo-tcu-proibe-francisco-araujo-de-ocupar-cargo-publico | N (imprensa) | [`2021-07_Metropoles_TCU_proibe_Francisco_Araujo_cargo_imprensa.html`](2021-07_Metropoles_TCU_proibe_Francisco_Araujo_cargo_imprensa.html) |
| idem | 07/2021 | DECISÃO (TCU, imprensa) | Inabilitação de Araújo e de mais 2 gestores por 8 anos, multa e glosa do contrato da Luna Park. O número do acórdão **não foi localizado**. | Multa de R$ 60 mil | idem | N (imprensa) | idem |
| idem | 13/02/2023 | DECISÃO (1ª instância federal) | **Absolvição sumária** de Araújo e de outros 14 réus, porque as provas foram consideradas ilícitas. O MP anunciou recurso. **O desfecho do recurso não foi localizado.** | — | https://blogs.correiobraziliense.com.br/cbpoder/justica-absolve-ex-secretario-de-saude-e-demais-denunciados-na-operacao-falso-negativo/ | N (imprensa) | 2023-02_CorreioBraziliense_*; 2023-02_AgendaCapital_* |
| **Paraíba**, cota no Consórcio Nordeste | 2022–2025 | ALEGAÇÃO (TCE-PB, citada no TCU) | Proposta de condenar o governador João Azevêdo e o secretário Geraldo Medeiros a ressarcir R$ 4,95 mi; aguardava o MP de Contas. **Desfecho não localizado.** | R$ 4.947.535,80 | Acórdão TCU 886/2025 | S | 2025-04-23_TCU_Acordao_886-2025-* |
| **Tabela oficial da PF** (estados e municípios) | 2020–2021 | FATO (operações; não são condenações) | **Ceará:** Dispneia (25/05/2020), respiradores, R$ 25,4 mi; Cartão Vermelho, R$ 7 mi. **Sergipe:** Serôdio (07/07/2020), hospital de campanha de Aracaju, R$ 3,26 mi. **Roraima:** Virion (13/08/2020), R$ 50 mi. **Divinópolis/MG:** Entre Amigos (11/12/2020), OS de UPA e hospital de campanha, R$ 100 mi. **Japeri/RJ:** Apneuse (06/10/2020), respiradores, R$ 2 mi. **Maranhão:** Falsa Esperança. **Municípios de SP:** Nudus, Protocletos, Involuto, Veneza e Medcruz. | ver tabela | URL da tabela PF | S | [`PF_tabela_operacoes_recursos_federais_COVID-19.html`](PF_tabela_operacoes_recursos_federais_COVID-19.html); [`PF_tabela_operacoes_COVID_extraida_DERIVADO.tsv`](PF_tabela_operacoes_COVID_extraida_DERIVADO.tsv) |

Os casos da tabela da PF foram listados como pistas. O desfecho judicial deles **não foi pesquisado**.

---

## Resumo de números e situação

| Caso | Contratado | Pago | Recuperado | Situação (out/2026) |
|---|---|---|---|---|
| Consórcio Nordeste / Hempcare | R$ 48.748.572,82 | R$ 48,7 mi (antecipado, 08/04/2020) | RN: R$ 3,57 mi (imprensa); total não localizado | TCU 886/2025 isentou os gestores (5 a 3) e abriu TCE contra a empresa. Inquérito no STJ (Inq 1426) sem denúncia localizada. Parecer do TCE-BA contra Rui Costa ainda não julgado. Ninguém condenado. |
| RJ / Witzel | Iabas: R$ 835,8 mi; PF: R$ 835 mi investigados | Iabas: R$ 256 mi até 11/05/2020 (imprensa) | não localizado | Impeachment definitivo (10 a 0, 30/04/2021). Réu em ação penal hoje no STJ, sem sentença. Habeas corpus no STF sem resultado localizado. |
| PA / Helder | R$ 50,4 mi | R$ 25,2 mi antecipados | governo diz que devolveu; sem documento oficial | Helder: arquivado pelo STJ (04/10/2023). 9 ex-auxiliares e empresários réus na Justiça Federal do PA desde 28/08/2025, sem sentença. |
| AM / Wilson Lima | R$ 2,976 mi (28 respiradores) | R$ 2,9 mi | não localizado | Réu na APn 993 desde 20/09/2021, sem mérito. Outra denúncia (frete) rejeitada em 2025. Agravos de 09/2026 com placar parcial de 9 a 0 contra a defesa. |
| SC / Veigamed | R$ 33 mi | R$ 33 mi (antecipado) | não localizado | Moisés absolvido (6 a 4, 07/05/2021). TCE-SC: contas irregulares e ressarcimento de R$ 33 mi (04/09/2023). Sentença cível nula e devolução de R$ 33 mi (07/2026, recorrível). Ação penal com 14 denunciados, prescrição parcial. |
| SP / Hichens | R$ 550.825.000,00 | R$ 242 mi antecipados (imprensa) | não localizado | TCE-SP (29/08/2023): dispensa regular e execução irregular. Desdobramentos no MP e na PF não localizados. |
| Recife / Apneia | R$ 11,5 mi | não localizado | não localizado | 6 réus desde 02/2025, sem sentença. |
| DF / Falso Negativo | — | — | — | 15 réus absolvidos sumariamente (02/2023). Recurso não localizado. TCU inabilitou gestores (imprensa). |

---

## Não localizado

1. **Consórcio Nordeste:**
   - total recuperado pelo Consórcio;
   - se houve sentença na ação de cobrança da Justiça da BA;
   - teor e efeito da decisão judicial 1059670-04.2025.4.01.3300/JFBA sobre o Acórdão 886/2025;
   - denúncia formal no Inq 1426/DF;
   - julgamento das contas de 2020 de Rui Costa pelo plenário do TCE-BA;
   - decisão do STF de Flávio Dino em documento oficial (só imprensa);
   - notas da PF sobre a Cianose (não baixadas: gov.br pede login).
2. **Witzel:**
   - sentença em qualquer ação penal;
   - resultado do habeas corpus no STF (Nunes Marques);
   - número público da ação no STJ (sigilo);
   - documento oficial do TJRJ ou da Alerj com a votação de 30/04/2021 (a confirmação oficial veio pela notícia do STJ de 05/05/2021);
   - valor recuperado do Iabas;
   - desfecho cível ou criminal contra o Iabas, Edmar Santos e Gabriell Neves (Operação Mercadores do Caos, MPRJ, com R$ 36,9 mi bloqueados segundo a imprensa).
3. **Pará:**
   - documento oficial do valor devolvido pela SKN;
   - nota oficial do MPF sobre a denúncia de 2025;
   - nota da PF sobre a Para Bellum (não baixada).
4. **Amazonas:**
   - proclamação oficial do julgamento dos agravos (02–08/09/2026);
   - valor recuperado;
   - julgamento do TCE-AM.
5. **Santa Catarina:**
   - íntegra da sentença cível de 07/2026 e valor exato do dano moral coletivo (a imprensa diverge);
   - valor já recuperado;
   - sentença na ação penal 5072303-77.2021.8.24.0023;
   - número e resultado da Operação O2/Oxigênio do MPSC em documento oficial.
6. **São Paulo:**
   - publicação do acórdão do TCE-SP no Diário Oficial e eventual recurso;
   - ação de reparação do MP-SP;
   - resultado da investigação da PF ("Operação Dragão", que não está na tabela oficial);
   - valor recuperado da Hichens.
7. **DF:** resultado da apelação contra a absolvição de 2023; número do acórdão do TCU.
8. **Recife:** sentença.
9. **Tabela da PF:** o desfecho dos demais casos (CE, SE, RR, MG, MA e municípios de SP) não foi pesquisado.


---
Cópias guardadas sem alteração. Impressão digital de cada arquivo em [`SHA256SUMS`](SHA256SUMS); origem, hora da coleta (UTC) e código HTTP em [`COLETA_LOG.tsv`](COLETA_LOG.tsv). Arquivos com `_imprensa` no nome são reportagens, não documentos oficiais.
