# Alterações no Notebook Principal

## Objetivo
Ajustar o Jupyter notebook principal para manter apenas as perguntas e respostas específicas solicitadas.

## Alterações Realizadas

### Notebook Reestruturado
O arquivo `1.6-Análise de Dados Olist.ipynb` foi completamente reestruturado para conter apenas as **4 perguntas específicas** solicitadas:

#### 1. Qual o percentual de pedidos entregues após a data estimada pela Olist?
- **Metodologia**: Filtrar pedidos entregues, calcular diferença entre data real e estimada
- **Visualizações**: Histograma de atrasos, pizza de distribuição, boxplot e resumo estatístico

#### 2. Qual o método de pagamento mais utilizado em pedidos acima de R$ 150,00?
- **Metodologia**: Filtrar por valor > R$ 150, agrupar por tipo de pagamento
- **Visualizações**: Gráficos de barras, pizza de distribuição, valor médio

#### 3. Qual é a relação entre o tempo de entrega e a nota de avaliação do cliente?
- **Metodologia**: Merge de datasets, cálculo de correlação de Pearson, remoção de outliers
- **Visualizações**: Scatter plot, boxplot, distribuição de tempos, tempo médio por nota

#### 4. Quais são as 5 categorias de produtos mais vendidas e qual a receita total gerada por cada uma?
- **Metodologia**: Merge order_items + products, agrupamento por categoria, ordenação por vendas
- **Visualizações**: Gráficos de barras, pizza de receita, ticket médio

## Estrutura do Novo Notebook

1. **Header institucional** (Unifor/Professor)
2. **Descrição do dataset** Olist
3. **Configuração inicial** (imports e setup)
4. **Carregamento de dados**
5. **4 Seções de análise** (uma para cada pergunta)
6. **Relatório final consolidado**
7. **Conclusões metodológicas**

## Arquivos

- **Original**: `1.6-Análise de Dados Olist-Original.ipynb` (backup do notebook original)
- **Novo**: `1.6-Análise de Dados Olist.ipynb` (versão focada nas 4 perguntas)
- **Alternativo**: `analise_duas_perguntas.ipynb` (versão com 2 perguntas que já existia)

## Funcionalidades Mantidas

- ✅ Compatibilidade com `data_loader.py`
- ✅ Geração de dados sintéticos para demonstração
- ✅ Visualizações completas e interativas
- ✅ Análises estatísticas detalhadas
- ✅ Interpretação dos resultados
- ✅ Metodologia documentada

## Compatibilidade

O notebook mantém total compatibilidade com:
- Sistema de dados existente (`data_loader.py`)
- Bibliotecas utilizadas (`pandas`, `matplotlib`, `seaborn`, etc.)
- Estrutura de dados do Olist
- Geração de dados sintéticos quando dados reais não estão disponíveis

## Benefícios da Reestruturação

1. **Foco**: Apenas as 4 perguntas solicitadas
2. **Clareza**: Estrutura mais limpa e direcionada
3. **Manutenibilidade**: Código mais organizado
4. **Reusabilidade**: Funções bem estruturadas para cada análise
5. **Didático**: Metodologia clara para cada questão