# Vacinação contra a Covid-19 por estado

Cópia de `doses_cobertura_proporcao_mes.csv`, baixada em 24/10/2026 de [covid19br/dados-vacinas](https://github.com/covid19br/dados-vacinas). É a soma, por estado, mês, faixa etária e situação vacinal, dos **microdados oficiais do SI-PNI** (Ministério da Saúde, OpenDataSUS), feita pelo **Observatório Covid-19 BR**, um grupo de pesquisadores. O agregado oficial do próprio Ministério (LocalizaSUS, OpenDataSUS) não pôde ser baixado deste ambiente.

Categorias: `D1cum` só 1ª dose; `D2cum` duas doses; `Dcum` dose única; `Rcum` com reforço. Cada pessoa está em uma categoria só. O campo `month` é o 1º dia do mês **seguinte** às aplicações (2021-07-01 = doses até 30/06/2021).

Como o site usa: ao menos 1 dose = D1cum + D2cum + Dcum + Rcum; esquema completo = D2cum + Dcum + Rcum; percentual sobre a população TCU 2019. Script: [`scripts/gerar_estados.py`](https://github.com/nk-ls/anatomia-do-caos/blob/main/scripts/gerar_estados.py).
