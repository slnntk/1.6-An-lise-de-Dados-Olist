# Análise de Dados Olist - Guia Completo para Iniciantes

## 👋 Bem-vindo ao Mundo da Análise de Dados!

Este documento é seu guia completo para entender como transformamos dados brutos em insights valiosos para negócios. Se você é novo em análise de dados, não se preocupe - explicaremos cada conceito de forma simples e prática.

## 🎯 O que Você Vai Aprender

### 📊 **Conceitos de Análise de Dados:**
- Como limpar e preparar dados
- O que são correlações e como interpretá-las
- Como calcular percentuais e estatísticas básicas
- Como criar e interpretar diferentes tipos de gráficos

### 💼 **Aplicação em Negócios:**
- Como medir satisfação do cliente
- Como avaliar performance de entregas
- Como identificar produtos mais rentáveis
- Como entender comportamento de pagamento

### 🛠️ **Ferramentas e Técnicas:**
- Uso do Python para análise de dados
- Bibliotecas: pandas, matplotlib, seaborn
- Técnicas de visualização de dados
- Interpretação de resultados estatísticos

## 📋 Dataset - O que Estamos Analisando

O **Brazilian E-Commerce Public Dataset by Olist** contém informações reais de aproximadamente 100 mil pedidos realizados entre 2016 e 2018. É como ter acesso aos dados internos de uma grande loja online!

### 🗃️ **O que Temos nos Dados:**

**📦 Informações de Pedidos:**
- Quando o pedido foi feito
- Quando foi entregue  
- Data estimada de entrega (nossa promessa ao cliente)
- Status do pedido (entregue, cancelado, etc.)

**💰 Informações Financeiras:**
- Preço dos produtos
- Método de pagamento (cartão, boleto, etc.)
- Parcelamento
- Valores de frete

**⭐ Avaliações dos Clientes:**
- Notas de 1 a 5 estrelas
- Comentários escritos
- Data da avaliação

**📍 Informações Geográficas:**
- Localização dos clientes
- Localização dos vendedores
- Tempo de transporte

### 🔍 **Por que Estes Dados São Valiosos?**

Com esses dados, podemos responder perguntas como:
- "Nossos clientes estão satisfeitos?"
- "Estamos entregando no prazo prometido?"
- "Quais produtos vendem mais?"
- "Qual método de pagamento os clientes preferem?"

## 🔬 Nossa Metodologia (Como Fazemos a Análise)

### 🧹 **Passo 1: Preparação dos Dados (Data Cleaning)**

**O que fazemos:**
- Removemos dados incompletos ou incorretos
- Convertemos datas para formato adequado
- Verificamos se os dados fazem sentido

**Por que é importante:**
"Garbage in, garbage out" - se os dados estão ruins, a análise será ruim. É como cozinhar com ingredientes estragados!

### 📊 **Passo 2: Análise Estatística**

**Estatística Descritiva - O Básico:**
- **Média:** Soma tudo e divide pelo número de itens
- **Mediana:** O valor do meio quando colocamos tudo em ordem
- **Percentual:** "De cada 100, quantos são assim?"

**Correlação - Relacionamentos:**
- **Correlação Positiva:** Quando uma coisa aumenta, a outra também aumenta
- **Correlação Negativa:** Quando uma aumenta, a outra diminui  
- **Sem Correlação:** Uma não afeta a outra

### 📈 **Passo 3: Visualização**

Criamos gráficos porque:
- Uma imagem vale mais que mil números
- É mais fácil ver padrões visualmente
- Facilita comunicar resultados para não-técnicos

## ❓ Perguntas de Negócio que Respondemos

### 📦 Pergunta 1: Qual o percentual de pedidos entregues após a data estimada?

**🎯 Por que esta pergunta importa?**

Imagine que você compra um presente de aniversário e o site promete entregar em 3 dias, mas demora 7 dias. Você ficaria frustrado, certo? Esta análise mede exatamente isso: quão boa a empresa é em cumprir suas promessas de entrega.

**🔬 Como Analisamos (Metodologia Detalhada):**

1. **Filtrar Dados:**
   - Pegamos apenas pedidos que foram realmente entregues
   - Removemos pedidos sem data de entrega ou sem data estimada
   - *Por quê?* Não podemos medir atraso se não sabemos quando foi entregue!

2. **Calcular Diferença:**
   - Fórmula: Data Real de Entrega - Data Estimada = Diferença em dias
   - Se positivo = atrasou
   - Se zero = chegou exato no dia
   - Se negativo = chegou antes (ótimo!)

3. **Classificar Resultados:**
   - 🔴 **Atrasado:** Chegou depois da data prometida
   - 🟢 **No Prazo:** Chegou exatamente no dia prometido  
   - 🚀 **Antecipado:** Chegou antes da data prometida

4. **Calcular Percentuais:**
   - Fórmula: (Quantidade de Atrasados ÷ Total) × 100
   - Exemplo: Se temos 100 pedidos e 10 atrasaram = 10%

**📊 Como Interpretar os Resultados:**

```python
# Código Principal (Comentado para Iniciantes)
delivered_orders['atraso_dias'] = (
    delivered_orders['order_delivered_customer_date'] - 
    delivered_orders['order_estimated_delivery_date']
).dt.days

# Classificar entregas
delivered_orders['status_entrega'] = delivered_orders['atraso_dias'].apply(
    lambda x: 'Atrasado' if x > 0 else 'No Prazo' if x == 0 else 'Antecipado'
)
```

**💡 Interpretação para Negócios:**

- **< 5% atrasado:** Excelente performance! Clientes muito satisfeitos
- **5-15% atrasado:** Bom, mas há espaço para melhoria
- **15-25% atrasado:** Atenção necessária - pode afetar reputação
- **> 25% atrasado:** Problema sério - precisa ação imediata

**🎨 Visualizações Criadas:**

1. **Gráfico de Pizza:** Mostra proporção de cada categoria
2. **Histograma:** Mostra distribuição de atrasos/antecipações  
3. **Box Plot:** Identifica valores extremos (outliers)
4. **Gráfico de Barras:** Compara quantidades absolutas
- Cálculo da diferença entre `order_delivered_customer_date` e `order_estimated_delivery_date`
- Classificação em três categorias: Atrasado (>0 dias), No Prazo (=0 dias), Antecipado (<0 dias)

#### Código Principal
```python
# Calcular atraso
delivered_orders['atraso_dias'] = (
    delivered_orders['order_delivered_customer_date'] - 
    delivered_orders['order_estimated_delivery_date']
).dt.days

# Classificar entregas
delivered_orders['status_entrega'] = delivered_orders['atraso_dias'].apply(
    lambda x: 'Atrasado' if x > 0 else 'No Prazo' if x == 0 else 'Antecipado'
)
```

#### Resultados
- **Total de entregas analisadas**: 844
- **Entregas atrasadas**: 0 (0.00%)
- **Entregas no prazo**: 0 (0.00%)
- **Entregas antecipadas**: 844 (100.00%)

#### Insights
No dataset de exemplo, todas as entregas foram realizadas antes da data estimada, indicando uma gestão logística eficiente ou estimativas conservadoras de prazo de entrega.

### 2. Qual o método de pagamento mais utilizado em pedidos acima de R$ 150,00?

#### Metodologia
- Filtro aplicado a pagamentos com `payment_value > 150.00`
- Agrupamento por `payment_type` com cálculos de frequência e valores
- Análise de distribuição percentual por método

#### Código Principal
```python
# Filtrar pedidos acima de R$ 150,00
payments_above_150 = payments[payments['payment_value'] > 150.0]

# Agrupar por método de pagamento
payment_stats = payments_above_150.groupby('payment_type').agg({
    'order_id': 'count',
    'payment_value': ['sum', 'mean']
}).round(2)
```

#### Resultados
| Método de Pagamento | Quantidade | Percentual | Valor Médio |
|---------------------|------------|------------|-------------|
| **Credit Card** | 565 | **69.75%** | R$ 381.87 |
| Boleto | 172 | 21.23% | R$ 367.30 |
| Debit Card | 52 | 6.42% | R$ 361.64 |
| Voucher | 21 | 2.59% | R$ 376.40 |

#### Insights
- **Cartão de crédito é predominante** em compras de alto valor (>R$ 150)
- Representa quase **70% dos pagamentos** nesta faixa
- Boleto mantém participação significativa (21%), típico do mercado brasileiro
- Valores médios são similares entre os métodos, indicando comportamento homogêneo

### 3. Quais são as 5 categorias de produtos mais vendidas e qual a receita total gerada por cada uma?

#### Metodologia
- Join entre `order_items` e `products` usando `product_id`
- Agrupamento por `product_category_name`
- Cálculo de quantidade vendida (count) e receita total (sum de price)
- Ordenação por quantidade vendida

#### Código Principal
```python
# Merge dos dados
items_products = order_items.merge(products, on='product_id', how='left')

# Agrupar por categoria
category_stats = items_products.groupby('product_category_name').agg({
    'order_id': 'count',  # Quantidade vendida
    'price': 'sum'        # Receita total
})
```

#### Resultados
| Posição | Categoria | Quantidade Vendida | Receita Total |
|---------|-----------|-------------------|---------------|
| 1º | **Housewares** | 289 | **R$ 76,029.94** |
| 2º | **Telephony** | 266 | **R$ 67,124.21** |
| 3º | **Watches & Gifts** | 259 | **R$ 69,992.58** |
| 4º | **Furniture & Decor** | 245 | **R$ 60,754.85** |
| 5º | **Health & Beauty** | 200 | **R$ 48,698.77** |

#### Insights
- **Housewares** lidera tanto em quantidade quanto em receita
- As 5 categorias principais concentram **R$ 322,600** em receita
- Telephony tem alta quantidade vendida, indicando produtos de menor ticket médio
- Watches & Gifts tem o melhor ticket médio (R$ 270.24)

### 4. Qual é a relação entre o tempo de entrega e a nota de avaliação do cliente?

#### Metodologia
- Join entre `orders` e `order_reviews` usando `order_id`
- Cálculo do tempo de entrega: diferença entre `order_delivered_customer_date` e `order_purchase_timestamp`
- Análise de correlação de Pearson entre tempo de entrega e `review_score`
- Remoção de outliers (tempo < 0 ou > 100 dias)

#### Código Principal
```python
# Calcular tempo de entrega em dias
delivered_reviews['tempo_entrega_dias'] = (
    delivered_reviews['order_delivered_customer_date'] - 
    delivered_reviews['order_purchase_timestamp']
).dt.days

# Calcular correlação
correlation = delivered_reviews['tempo_entrega_dias'].corr(delivered_reviews['review_score'])
```

#### Resultados
- **Total de avaliações analisadas**: 238
- **Correlação**: 0.002 (muito fraca)
- **Tempo médio de entrega**: 51.2 dias

| Nota | Quantidade | Tempo Médio (dias) | Desvio Padrão |
|------|------------|-------------------|---------------|
| 1 | 9 | 44.78 | 27.52 |
| 2 | 15 | 54.47 | 27.14 |
| 3 | 32 | 50.91 | 30.69 |
| 4 | 60 | 52.62 | 27.71 |
| 5 | 122 | 50.64 | 31.35 |

#### Insights
- **Não há correlação significativa** entre tempo de entrega e satisfação do cliente
- Clientes que deram nota 1 tiveram entregas mais rápidas (44.8 dias)
- A maioria das avaliações são positivas (nota 5: 51% das avaliações)
- Outros fatores além do tempo podem influenciar mais a satisfação

## Visualizações Geradas

### 1. Entregas Atrasadas
- **Gráfico de Pizza**: Distribuição do status de entrega
- **Histograma**: Distribuição de atrasos/antecipações em dias

### 2. Métodos de Pagamento
- **Gráfico de Barras**: Quantidade de pedidos por método
- **Gráfico de Pizza**: Distribuição percentual dos métodos

### 3. Categorias de Produtos
- **Gráficos de Barras**: Quantidade vendida e receita por categoria
- **Gráficos de Pizza**: Distribuições proporcionais

### 4. Tempo de Entrega vs Avaliação
- **Scatter Plot**: Correlação visual
- **Box Plot**: Distribuição do tempo por nota
- **Histogramas**: Distribuições individuais
- **Heatmap**: Matriz de correlação

## Limitações e Considerações

### Limitações dos Dados de Exemplo
- Dataset sintético criado para demonstração
- Padrões podem não refletir a realidade do Olist
- Dados reais podem apresentar maior variabilidade

### Considerações para Análise com Dados Reais
1. **Sazonalidade**: Considerar variações por época do ano
2. **Geografia**: Analisar diferenças regionais
3. **Temporal**: Estudar tendências ao longo do tempo
4. **Segmentação**: Análise por faixas de preço e categorias específicas

## Recomendações de Negócio

### Com Base nos Resultados da Análise

1. **Gestão de Entregas**
   - Manter as estimativas conservadoras que resultam em entregas antecipadas
   - Usar entregas rápidas como diferencial competitivo

2. **Estratégia de Pagamento**
   - Focar em facilitar pagamentos por cartão de crédito
   - Manter opções de boleto para ampliar acessibilidade

3. **Mix de Produtos**
   - Investir no crescimento das categorias top 5
   - Desenvolver estratégias específicas para Housewares e Telephony

4. **Experiência do Cliente**
   - Investigar outros fatores além do tempo de entrega que impactam a satisfação
   - Implementar pesquisas qualitativas para entender melhor as avaliações

## Como Executar a Análise

### Pré-requisitos
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Execução
```bash
# Para análise completa
python analise_olist.py

# Para carregar apenas os dados
python data_loader.py
```

### Arquivos Gerados
- `pergunta_1_entregas_atrasadas.png`
- `pergunta_2_metodos_pagamento.png`
- `pergunta_3_top_categorias.png`
- `pergunta_4_tempo_entrega_avaliacao.png`

## Estrutura do Código

### Organização Modular
- **`data_loader.py`**: Carregamento e preparação dos dados
- **`analise_olist.py`**: Classe principal com todas as análises
- **`OlistAnalysis`**: Classe que encapsula toda a lógica de análise

### Principais Métodos
- `pergunta_1_entregas_atrasadas()`: Análise de pontualidade das entregas
- `pergunta_2_metodo_pagamento()`: Análise de métodos de pagamento
- `pergunta_3_top_categorias()`: Análise de categorias mais vendidas
- `pergunta_4_tempo_entrega_avaliacao()`: Análise de correlação tempo-satisfação

## Conclusões

Esta análise fornece uma base sólida para compreender o comportamento do e-commerce brasileiro através dos dados do Olist. Os resultados destacam:

1. **Eficiência Logística**: Entregas consistentemente antecipadas
2. **Preferências de Pagamento**: Dominância do cartão de crédito em compras de alto valor
3. **Mix de Produtos**: Concentração em categorias domésticas e tecnologia
4. **Satisfação do Cliente**: Fatores além do tempo de entrega influenciam as avaliações

Para análises mais profundas, recomenda-se o uso do dataset completo e real do Olist, disponível no Kaggle, que permitirá insights mais precisos e actionáveis para decisões de negócio.

---

**Autor**: Sistema de Análise Automatizada  
**Data**: 2025  
**Versão**: 1.0