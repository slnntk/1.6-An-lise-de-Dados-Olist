# Análise Completa de Dados Olist - Ciência de Dados

## 1. Introdução

O **Brazilian E-Commerce Public Dataset by Olist** é um conjunto de dados transacionais de um marketplace brasileiro, contendo informações de aproximadamente 100 mil pedidos realizados entre 2016 e 2018. Esta análise visa responder 5 perguntas fundamentais sobre o comportamento do e-commerce brasileiro usando técnicas de ciência de dados.

## 2. Dataset e Metodologia

O dataset contém informações sobre:
- **Orders**: Dados dos pedidos (status, datas, etc.)
- **Customers**: Informações dos clientes e localização
- **Order Items**: Itens dos pedidos (produtos, preços, frete)
- **Products**: Informações dos produtos
- **Sellers**: Informações dos vendedores
- **Reviews**: Avaliações dos clientes
- **Payments**: Formas de pagamento
- **Geolocation**: Dados geográficos dos códigos postais

## 3. Análise das 5 Perguntas Centrais

### Pergunta 1: Quantas vendas foram realizadas durante todo o período do dataset?

**Resposta**: Foram realizadas **99.441 vendas** no período de 2016 a 2018.

**Insights**:
- Cada pedido representa uma transação única no marketplace
- O volume indica um marketplace de médio porte em crescimento
- Período de análise de aproximadamente 2 anos fornece base sólida para análises sazonais

### Pergunta 2: Quantos pedidos existem para cada status?

**Resposta**:
- **Delivered**: 96.476 pedidos (97.02%)
- **Shipped**: 1.107 pedidos (1.11%)
- **Canceled**: 625 pedidos (0.63%)
- **Unavailable**: 609 pedidos (0.61%)
- **Invoiced**: 314 pedidos (0.32%)
- **Processing**: 301 pedidos (0.30%)
- **Created**: 5 pedidos (0.005%)
- **Approved**: 2 pedidos (0.002%)

**Insights**:
- Taxa de entrega muito alta (97%), indicando eficiência operacional
- Taxa de cancelamento baixa (0.63%), sugerindo boa qualidade do serviço
- Poucos pedidos em processamento, indicando agilidade no fulfillment

### Pergunta 3: Qual a distribuição temporal dos pedidos ao longo do período?

**Resposta**:
- **2016**: 329 pedidos (0.33%)
- **2017**: 45.101 pedidos (45.35%)  
- **2018**: 54.011 pedidos (54.32%)

**Crescimento**: Explosivo crescimento de 13.607% de 2016 para 2017, seguido de crescimento sólido de 19.8% de 2017 para 2018.

**Padrões Temporais**:
- **Pico de horário**: 20h (horário de maior atividade de compras online)
- **Melhor dia da semana**: Segunda-feira
- **Sazonalidade**: Picos em novembro (Black Friday) e janeiro

**Insights**:
- Marketplace em fase de crescimento acelerado
- Comportamento típico de e-commerce brasileiro com pico noturno
- Oportunidade de campanhas direcionadas nos horários de pico

### Pergunta 4: Como se comporta a distribuição geográfica dos clientes e vendas?

**Resposta**:

**Top 5 Estados**:
1. **São Paulo (SP)**: 41.746 clientes (41.7%)
2. **Rio de Janeiro (RJ)**: 12.852 clientes (12.9%)  
3. **Minas Gerais (MG)**: 11.635 clientes (11.6%)
4. **Rio Grande do Sul (RS)**: 5.466 clientes (5.5%)
5. **Paraná (PR)**: 5.045 clientes (5.0%)

**Concentração Regional**:
- **Sudeste**: Domina com ~66% dos clientes
- **Sul**: Segunda região com ~15% dos clientes  
- **Nordeste**: ~14% dos clientes
- **Centro-Oeste** e **Norte**: Menor penetração

**Insights**:
- Fortíssima concentração no eixo SP-RJ-MG (66% dos clientes)
- 6 estados concentram 80% dos clientes
- Grande oportunidade de expansão no Nordeste e Norte
- São Paulo sozinho representa 42% de toda a base

### Pergunta 5: Qual o perfil dos produtos mais vendidos e a distribuição de valores?

**Análise de Pareto dos Produtos**:
- **67.65% do faturamento** advém dos **20% dos produtos mais vendidos**
- Confirmação clara do princípio 80/20 no e-commerce

**Análise de Ticket Médio**:
- **Ticket médio (produtos)**: R$ 103,00
- **Ticket médio (total com frete)**: R$ 137,75
- **Frete médio**: R$ 19,99
- **Itens por pedido**: 1,2 itens

**Distribuição de Valores**:
- **Mediana**: R$ 108,00 (valor mais comum)
- **25º percentil**: R$ 67,00
- **75º percentil**: R$ 168,00
- **95º percentil**: R$ 315,00

**Insights**:
- Frete representa ~14.5% do valor total do pedido
- Distribuição assimétrica com cauda longa (alguns pedidos de alto valor)
- Maioria dos pedidos concentrada na faixa R$ 50-150
- Estratégia de frete grátis pode ser viável para pedidos > R$ 150

## 4. Recomendações Estratégicas

1. **Excelência Operacional**: Manter a alta taxa de entrega (97%)
2. **Análise Geográfica**: Expandir para regiões com menor cobertura
3. **Gestão de Produtos**: Focar nos produtos que geram 67.65% do faturamento
4. **Sazonalidade**: Preparar-se para picos identificados na análise temporal
5. **Qualidade do Serviço**: Manter baixa taxa de cancelamento através de melhoria contínua

## 5. Conclusões

O marketplace Olist demonstra indicadores saudáveis de operação, com alta eficiência na entrega e baixas taxas de cancelamento. A análise revela oportunidades de otimização baseadas na concentração de produtos rentáveis e na compreensão dos padrões temporais e geográficos de compra.

A aplicação do princípio de Pareto (80/20) é claramente observada nos dados, onde aproximadamente 20% dos produtos são responsáveis por quase 68% do faturamento, orientando estratégias de estoque e marketing.

---

*Análise realizada usando Python, Pandas, Numpy, Matplotlib e técnicas de ciência de dados.*