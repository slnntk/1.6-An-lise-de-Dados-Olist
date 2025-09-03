# Notebook: Análise das Duas Perguntas Específicas

O notebook `analise_duas_perguntas.ipynb` foi criado para responder especificamente a duas perguntas sobre o dataset do Olist:

## Pergunta 1: Relação entre Tempo de Entrega e Avaliação do Cliente
- **Metodologia**: Merge entre tabelas `orders` e `order_reviews`, cálculo do tempo de entrega em dias, análise de correlação de Pearson
- **Lógica**: Calculamos a diferença entre a data de entrega real e a data de compra, removemos outliers extremos, e analisamos a correlação com as notas de avaliação
- **Visualizações**: Scatter plot, box plot, histograma e gráfico de barras das médias

## Pergunta 2: Top 5 Categorias de Produtos Mais Vendidas
- **Metodologia**: Merge entre `order_items` e `products`, agrupamento por categoria, cálculo de quantidade vendida e receita total
- **Lógica**: Agrupamos os dados por categoria de produto, calculamos métricas de vendas e receita, ordenamos por quantidade vendida e selecionamos as top 5
- **Visualizações**: Gráficos de barras, gráfico de pizza e análise de ticket médio

## Como Executar

1. Certifique-se de que as dependências estão instaladas: `pip install -r requirements.txt`
2. Execute o notebook: `jupyter notebook analise_duas_perguntas.ipynb`
3. Execute todas as células sequencialmente

## Dados
O notebook utiliza a função `load_data()` do arquivo `data_loader.py`, que automaticamente carrega dados de exemplo caso os dados reais do Olist não estejam disponíveis.

## Resultados
O notebook gera:
- Análises estatísticas detalhadas
- Visualizações interativas
- Interpretações dos resultados
- Conclusões práticas para cada pergunta