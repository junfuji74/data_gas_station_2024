# data_gas_station_2024
Analise de dados de abastecimentos de uma rede de combustíveis do ABC paulista no ano de 2024


# 📊 Análise de Abastecimentos Acima de R$100 em Rede de Postos de Combustível

Este projeto tem como objetivo analisar os padrões de abastecimentos acima de R$100 realizados ao longo do ano de 2024 em uma rede de postos de combustíveis. Os dados foram extraídos de uma view SQL tratada previamente, e a análise foi realizada com foco na identificação de sazonalidade, comportamento de clientes e variações de valor.

---

## 🗂️ Estrutura dos Dados

A base de dados contém mais de **500 mil registros**, com as seguintes colunas principais:
- `data_venda`: Data do abastecimento
- `valor_total`: Valor total pago no abastecimento
- `posto_cnpj`: Identificador do posto de combustível
- `customer_id`: Identificador (hash) do cliente
- `status`: Todos os registros com status **aprovado**

---

## 🔎 Filtro inicial: Abastecimentos acima de R$100

Foi aplicado um filtro para considerar apenas os abastecimentos com **valor acima de R$100**, totalizando:

📌 **134.987 abastecimentos filtrados**

---

## 📅 Sazonalidade por mês

A análise dos meses com maior volume de abastecimentos acima de R$100 revelou os seguintes resultados:

| Mês  | Abastecimentos |
|------|----------------|
| Maio (5)  | 12.519 |
| Agosto (8) | 12.215 |
| Novembro (11) | 12.607 |

**Interpretação:**  
Esses picos podem indicar momentos do ano com maior movimentação econômica, aumento no fluxo de veículos ou **eventos promocionais** que estimularam o consumo nesses períodos.

---

## 🛒 Top 10 Postos com Mais Abastecimentos

| CNPJ do Posto       | Total de Abastecimentos |
|----------------------|--------------------------|
| 47290002000126       | 15.711                   |
| 12044737000195       | 13.527                   |
| 08196281000101       | 11.636                   |
| ...                  | ...                      |

**Análise:**  
Esses postos podem ter tido maior destaque na campanha de prêmios promovida pela rede, seja por localização estratégica, divulgação ou tamanho da unidade.

---

## 👤 Top 10 Clientes com Mais Abastecimentos

| Cliente (ID hash)                         | Abastecimentos |
|------------------------------------------|----------------|
| 4afac311-80b4-4236-9103-e21cf9d43718      | 303            |
| c8649f06-e374-4ef8-9457-7cbe6b424b04      | 239            |
| fdf8b5dd-e0c4-4f0a-a6b3-068003662b64      | 216            |
| ...                                      | ...            |

**Interpretação:**  
Clientes com mais de 200 abastecimentos em um ano com valor acima de R$100 demonstram comportamento atípico. Possivelmente são **empresas com frotas** ou usuários com uso intensivo de combustível. Essa informação pode ser útil para abordagens comerciais personalizadas.

---

## 💰 Distribuição por Faixa de Valor

Foi feita a segmentação dos abastecimentos filtrados em faixas de valor:

| Faixa de Valor (R$) | Quantidade de Abastecimentos | Interpretação |
|---------------------|-------------------------------|----------------|
| 100–300             | 130.269                       | Perfil comum de cliente físico buscando participar da campanha |
| 301–600             | 4.194                         | Veículos de maior porte ou maior frequência |
| 601–1000            | 267                           | Frotas leves ou uso comercial |
| 1001–3000           | 155                           | Frotas maiores, vans, ônibus |
| 3001+               | 102                           | Abastecimentos **fora da curva**, indicam caminhões ou veículos de transporte pesado |

---

A análise do ticket médio revelou diferenças importantes no perfil de consumo entre os postos da rede. O posto com CNPJ 45949344000180 apresentou o maior ticket médio em 2024, com R$124,91 por abastecimento. Esse valor, consideravelmente superior à média dos demais, pode estar relacionado à localização estratégica do posto, atendimento a veículos maiores, ou até mesmo à fidelização de clientes com alto consumo. Na sequência, os postos 3618954000150 (R$115,05) e 47290002000126 (R$103,79) também demonstraram desempenhos notáveis. Vale destacar que o posto 47290002000126, que já havia se sobressaído em volume total de vendas, figura entre os três com maior ticket médio, reforçando a hipótese de que esse ponto específico tenha exercido um papel central durante a campanha de premiação promovida pela rede.


## 📌 Conclusões

- A campanha da rede parece ter sido eficaz para **engajar clientes comuns**, mantendo um bom volume de abastecimentos acima de R$100.
- Foi possível identificar **clientes corporativos** com alta recorrência, o que permite um estudo mais aprofundado sobre fidelização e comportamento.
- Alguns abastecimentos apresentam valores extremos, indicando a existência de veículos pesados e possíveis oportunidades para **condições comerciais diferenciadas** para empresas.
- Postos com maior volume de abastecimentos podem servir de **modelo de boas práticas** para outras unidades da rede.

---
