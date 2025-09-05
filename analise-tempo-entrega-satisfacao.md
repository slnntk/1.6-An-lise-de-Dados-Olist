# 📊 Análise: Tempo de Entrega vs Satisfação do Cliente

## 🎯 Objetivo da Análise
Este código investiga se existe uma relação entre o tempo que um pedido demora para ser entregue e a nota que o cliente dá na avaliação. É uma pergunta fundamental para qualquer e-commerce!

## 📋 Código Comentado Passo a Passo

### 1. Preparação dos Dados
```python
# Carregar datasets necessários
orders = pd.read_csv(os.path.join(path, 'olist_orders_dataset.csv'))
reviews = pd.read_csv(os.path.join(path, 'olist_order_reviews_dataset.csv'))
```

**💡 O que faz:**
- Carrega duas "planilhas" de dados:
  - `orders`: informações sobre pedidos (quando foi feito, quando foi entregue)
  - `reviews`: avaliações dos clientes (nota de 1 a 5 estrelas)

**🤔 Por que precisa de duas tabelas?**
- Os dados estão separados por organização
- Uma tabela tem info de logística, outra tem info de satisfação
- Precisamos "juntar" essas informações

### 2. Conversão de Datas
```python
# Converter datas
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
```

**💡 O que faz:**
- Transforma textos como "2017-10-02 10:56:33" em datas que o computador entende
- Permite fazer cálculos matemáticos com datas (subtrair, somar dias, etc.)

**🤔 Por que é importante?**
- Datas em texto: "não dá para calcular 10/10/2023 - 05/10/2023"
- Datas convertidas: "permite calcular que são 5 dias de diferença"

### 3. Juntando as Informações (JOIN)
```python
# Merge entre pedidos e avaliações
orders_reviews = orders.merge(reviews, on='order_id', how='inner')
```

**💡 O que faz:**
- Junta as duas tabelas usando o "código do pedido" como chave
- Resultado: uma tabela com TUDO (data da compra, entrega E nota da avaliação)

**🤔 Analogia:**
- Imagine duas listas: uma com "João - Pedido 123" e outra com "Pedido 123 - Nota 5"
- O merge junta: "João - Pedido 123 - Nota 5"

### 4. Filtros de Qualidade
```python
# Filtrar apenas pedidos entregues com datas válidas
delivered_reviews = orders_reviews[
    (orders_reviews['order_status'] == 'delivered') &
    (orders_reviews['order_delivered_customer_date'].notna()) &
    (orders_reviews['order_purchase_timestamp'].notna()) &
    (orders_reviews['review_score'].notna())
].copy()
```

**💡 O que faz:**
- Remove "lixo" dos dados:
  - ❌ Pedidos cancelados ou não entregues
  - ❌ Pedidos sem data de entrega
  - ❌ Pedidos sem avaliação
- Fica só com dados "limpos" e confiáveis

**🤔 Por que filtrar?**
- Dados ruins = conclusões erradas
- Queremos analisar apenas pedidos que realmente foram entregues E avaliados

### 5. Criação da Variável Principal
```python
# Calcular tempo de entrega em dias
delivered_reviews['tempo_entrega_dias'] = (
    delivered_reviews['order_delivered_customer_date'] - 
    delivered_reviews['order_purchase_timestamp']
).dt.days
```

**💡 O que faz:**
- Calcula quantos dias passaram entre a compra e a entrega
- Exemplo: Comprou 01/01, entregou 05/01 = 4 dias

**🤔 Fórmula simples:** 
```
Tempo de Entrega = Data da Entrega - Data da Compra
```

### 6. Remoção de Outliers
```python
# Remover outliers extremos (tempo de entrega negativo ou muito alto)
delivered_reviews = delivered_reviews[
    (delivered_reviews['tempo_entrega_dias'] >= 0) & 
    (delivered_reviews['tempo_entrega_dias'] <= 100)
]
```

**💡 O que faz:**
- Remove casos "impossíveis":
  - �� Tempo negativo (entregou antes de comprar? Erro nos dados!)
  - ❌ Mais de 100 dias (provavelmente erro ou caso excepcional)

**🤔 Por que remover?**
- Casos extremos podem "enganar" a análise
- 99% dos pedidos chegam em menos de 100 dias

### 7. Análise Estatística
```python
# Calcular estatísticas por nota de avaliação
stats_by_score = delivered_reviews.groupby('review_score')['tempo_entrega_dias'].agg([
    'count', 'mean', 'median', 'std'
]).round(2)
```

**💡 O que faz:**
- Separa os dados por nota (1⭐, 2⭐, 3⭐, 4⭐, 5⭐)
- Para cada nota, calcula:
  - `count`: quantas avaliações
  - `mean`: tempo médio de entrega
  - `median`: tempo "do meio" (50% entrega mais rápido, 50% mais devagar)
  - `std`: o quanto varia (todos entregam em 10 dias ou varia muito?)

**🤔 Exemplo do resultado:**
```
1⭐ (insatisfeitos): 20,5 dias em média
5⭐ (satisfeitos):   10,2 dias em média
```

### 8. Cálculo da Correlação
```python
# Calcular correlação
correlation = delivered_reviews['tempo_entrega_dias'].corr(delivered_reviews['review_score'])
```

**💡 O que faz:**
- Calcula um número entre -1 e +1 que mostra se existe relação entre tempo e nota
  - `-1`: relação perfeita negativa (mais tempo = menos satisfação)
  - `0`: não há relação nenhuma
  - `+1`: relação perfeita positiva (mais tempo = mais satisfação)

**🤔 Como interpretar:**
- `-0.349` (como no exemplo): relação moderada negativa
- Significa: "geralmente, mais tempo de entrega resulta em nota mais baixa"

## 🎯 O que o Código Descobriu

### Resultado Principal:
```python
print(f"Correlação entre tempo de entrega e nota: {correlation:.3f}")
```

Se der `-0.349`, significa:
- ✅ **Existe relação**: tempo impacta satisfação
- ✅ **Relação moderada**: nem fraca, nem muito forte
- ✅ **Direção negativa**: mais tempo = menos satisfação

### Exemplo Prático dos Resultados:
```
Clientes que deram 1⭐: pedidos demoraram 20,5 dias em média
Clientes que deram 5⭐: pedidos demoraram 10,2 dias em média
Diferença: 10+ dias a mais para insatisfeitos!
```

## 💡 Insights para Negócio

### O que isso significa na prática:

**📈 Tempo importa para satisfação**
- Não é o único fator, mas é importante
- Clientes insatisfeitos esperam quase o dobro do tempo

**🎯 Meta de entrega**
- Tentar entregar em até 10 dias
- Acima de 15 dias = alto risco de insatisfação

**💰 ROI de melhorias logísticas**
- Investir em entregas mais rápidas pode melhorar avaliações
- Clientes satisfeitos compram mais vezes

## 🔍 Limitações da Análise

O código não considera:
- 🚚 Tipo de produto (urgente vs não-urgente)
- 📍 Região (interior vs capital)
- 💵 Valor do pedido (produto caro vs barato)
- 📅 Época do ano (Black Friday vs período normal)

### Para análise mais completa:
```python
# Próximos passos sugeridos
analise_por_regiao = delivered_reviews.groupby('customer_state')['tempo_entrega_dias'].mean()
analyse_por_categoria = delivered_reviews.groupby('product_category')['review_score'].mean()
```

## 📊 Visualização dos Resultados

Para ver graficamente:
```python
import matplotlib.pyplot as plt

# Gráfico: Tempo médio por nota
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Tempo médio por nota
tempo_por_nota = delivered_reviews.groupby('review_score')['tempo_entrega_dias'].mean()
ax1.bar(['1⭐', '2⭐', '3⭐', '4⭐', '5⭐'], tempo_por_nota.values, 
        color=['red', 'orange', 'yellow', 'lightgreen', 'green'])
ax1.set_title('Tempo Médio de Entrega por Nota')
ax1.set_ylabel('Dias')

# Gráfico 2: Dispersão
ax2.scatter(delivered_reviews['tempo_entrega_dias'], delivered_reviews['review_score'], alpha=0.5)
ax2.set_xlabel('Tempo de Entrega (dias)')
ax2.set_ylabel('Nota da Avaliação')
ax2.set_title(f'Correlação: {correlation:.3f}')

plt.tight_layout()
plt.show()
```

## ✅ Resumo em Linguagem Simples

**Pergunta:** "Pedidos que demoram mais para chegar recebem notas piores?"

**Resposta:** "Sim! A análise de 96.293 pedidos mostrou que:"

- 📊 Correlação de -0.349 (relação moderada)
- ⏱️ Clientes insatisfeitos esperaram 10+ dias a mais
- 🎯 Tempo explica ~12% da satisfação (outros fatores também importam)

**Ação recomendada:** "Investir em logística mais rápida pode melhorar as avaliações, mas também considerar outros fatores como qualidade do produto e atendimento."

---

**Este código é um exemplo excelente de como transformar dados brutos em insights de negócio acionáveis!** 🚀

## 📂 Código Completo

```python
# Análise: Relação entre Tempo de Entrega e Satisfação do Cliente

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Carregamento dos dados
path = 'caminho/para/os/dados'  # Ajuste conforme necessário
orders = pd.read_csv(os.path.join(path, 'olist_orders_dataset.csv'))
reviews = pd.read_csv(os.path.join(path, 'olist_order_reviews_dataset.csv'))

# 2. Conversão de datas
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])

# 3. Merge entre pedidos e avaliações
orders_reviews = orders.merge(reviews, on='order_id', how='inner')

# 4. Filtros de qualidade
delivered_reviews = orders_reviews[
    (orders_reviews['order_status'] == 'delivered') &
    (orders_reviews['order_delivered_customer_date'].notna()) &
    (orders_reviews['order_purchase_timestamp'].notna()) &
    (orders_reviews['review_score'].notna())
].copy()

# 5. Cálculo do tempo de entrega
delivered_reviews['tempo_entrega_dias'] = (
    delivered_reviews['order_delivered_customer_date'] - 
    delivered_reviews['order_purchase_timestamp']
).dt.days

# 6. Remoção de outliers
delivered_reviews = delivered_reviews[
    (delivered_reviews['tempo_entrega_dias'] >= 0) & 
    (delivered_reviews['tempo_entrega_dias'] <= 100)
]

# 7. Análise estatística
stats_by_score = delivered_reviews.groupby('review_score')['tempo_entrega_dias'].agg([
    'count', 'mean', 'median', 'std'
]).round(2)

# 8. Correlação
correlation = delivered_reviews['tempo_entrega_dias'].corr(delivered_reviews['review_score'])

# 9. Resultados
print("=" * 60)
print("ANÁLISE: TEMPO DE ENTREGA vs SATISFAÇÃO DO CLIENTE")
print("=" * 60)
print(f"\nTotal de pedidos analisados: {len(delivered_reviews):,}")
print(f"Correlação entre tempo e nota: {correlation:.3f}")
print(f"Interpretação: {'Relação moderada negativa' if correlation < -0.3 else 'Relação fraca'}")
print("\nEstatísticas por nota de avaliação:")
print(stats_by_score)
```

## 📚 Dataset Utilizado

**Fonte:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/)

**Principais tabelas utilizadas:**
- `olist_orders_dataset.csv`: Dados dos pedidos
- `olist_order_reviews_dataset.csv`: Avaliações dos clientes

## 🏆 Conclusões Finais

Esta análise demonstra claramente que **o tempo de entrega é um fator crítico para a satisfação do cliente**. Empresas que desejam melhorar suas avaliações devem priorizar a otimização de seus processos logísticos.

### Próximos Passos Recomendados:
1. **Análise por região**: Identificar estados com maiores problemas de entrega
2. **Análise por categoria**: Verificar se produtos específicos têm problemas logísticos
3. **Análise temporal**: Entender se há sazonalidade nos tempos de entrega
4. **Análise de valor**: Verificar se o valor do pedido influencia a tolerância ao tempo de entrega
