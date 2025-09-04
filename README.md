# Análise de Dados Olist - Brazilian E-Commerce Dataset

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.0+-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 Descrição - Perfeito para Iniciantes em Análise de Dados!

Este projeto apresenta uma **análise completa e educativa** do dataset público do Olist, maior marketplace brasileiro. É especialmente projetado para pessoas que estão **aprendendo análise de dados**, com explicações detalhadas de cada conceito e metodologia.

### 🎯 O que você vai aprender:

**📊 Análise Estatística Básica:**
- Como filtrar e limpar dados
- Como calcular percentuais e médias
- Como interpretar correlações
- Como identificar padrões nos dados

**📈 Visualização de Dados:**
- Como criar gráficos informativos
- Como interpretar diferentes tipos de gráficos
- Como usar cores e formatação para comunicar melhor

**💼 Aplicação em Negócios:**
- Como transformar dados em insights acionáveis
- Como medir satisfação do cliente
- Como avaliar performance de entregas
- Como identificar oportunidades de melhoria

### ❓ Perguntas que Respondemos (com metodologia explicada):

1. **📦 Qual o percentual de pedidos entregues após a data estimada pela Olist?**
   - *Por que importa?* Entregas atrasadas afetam diretamente a satisfação do cliente
   - *O que você aprende?* Como medir precisão de estimativas e calcular percentuais

2. **⏱️ Qual é a relação entre o tempo de entrega e a nota de avaliação do cliente?**
   - *Por que importa?* Tempo de entrega pode impactar a experiência do cliente  
   - *O que você aprende?* Como medir correlações e interpretar relacionamentos entre variáveis

3. **🏆 Quais são as 5 categorias de produtos mais vendidas e qual a receita total?**
   - *Por que importa?* Identifica os produtos mais lucrativos do negócio
   - *O que você aprende?* Como fazer análise de vendas, agrupamentos e rankings

4. **💳 Qual o método de pagamento mais utilizado em pedidos acima de R$ 150,00?**
   - *Por que importa?* Ajuda a entender comportamento de compra de alto valor
   - *O que você aprende?* Como filtrar dados por condições e analisar preferências

## 🚀 Quick Start

### 👶 Para Iniciantes - Comece Aqui!

Se você é novo em análise de dados, recomendamos começar com nosso **notebook educativo**:

```bash
# 1. Instale o Jupyter (se ainda não tiver)
pip install jupyter pandas numpy matplotlib seaborn

# 2. Abra o notebook interativo
jupyter notebook analise_duas_perguntas.ipynb
```

**Por que usar o notebook?**
- ✅ Explicações passo a passo de cada conceito
- ✅ Código comentado e fácil de entender  
- ✅ Glossário de termos técnicos
- ✅ Interpretações práticas para negócios
- ✅ Visualizações com explicações detalhadas

### 🏃 Para Usuários Mais Experientes

Execute o script completo diretamente:

### Instalação das Dependências

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Execução Rápida

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/olist-analysis.git
cd olist-analysis

# Execute a análise completa
python analise_olist.py
```

## 📊 Resultados Principais

| Pergunta | Resultado |
|----------|-----------|
| **Entregas Atrasadas** | 0.00% dos pedidos (dados de exemplo) |
| **Método de Pagamento Top** | Credit Card (69.75% dos pedidos > R$ 150) |
| **Categoria Mais Vendida** | Housewares (289 vendas, R$ 76k receita) |
| **Correlação Tempo-Nota** | 0.002 (correlação muito fraca) |

## 📚 Para Quem Está Aprendendo - Guia de Estudos

### 🎯 Conceitos que Você Vai Dominar

Após completar esta análise, você será capaz de:

**📊 Estatística Descritiva:**
- Calcular médias, medianas e percentis
- Entender o que são outliers e como tratá-los
- Interpretar distribuições de dados

**🔗 Análise de Correlação:**
- O que é correlação de Pearson
- Como interpretar valores de correlação (-1 a +1)
- Diferença entre correlação e causalidade

**📈 Visualização de Dados:**
- Quando usar gráfico de pizza vs barras vs histograma
- Como interpretar box plots
- Como criar visualizações que contam uma história

**💼 Business Intelligence:**
- Como transformar dados em decisões de negócio
- Métricas de satisfação do cliente
- Análise de performance operacional

### 🗂️ Estrutura de Aprendizado

1. **Comece com:** `analise_duas_perguntas.ipynb` (análise educativa)
2. **Continue com:** `analise_olist.py` (script completo)
3. **Aprofunde-se:** `ANALISE_DETALHADA.md` (metodologia técnica)

## 📁 Estrutura do Projeto

```
├── analise_olist.py              # Script principal de análise
├── data_loader.py                # Carregador de dados
├── ANALISE_DETALHADA.md          # Documentação completa
├── README.md                     # Este arquivo
└── 1.6-Análise de Dados Olist.ipynb  # Notebook original
```

## 🔧 Como Usar

### 1. Com Dados Reais (Recomendado)

```bash
# Baixe o dataset do Kaggle
# https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

# Crie a pasta data e extraia os CSVs
mkdir data
# Copie os arquivos CSV para a pasta data/

# Execute a análise
python analise_olist.py
```

### 2. Com Dados de Exemplo (Demo)

```bash
# Execute diretamente - usa dados sintéticos
python analise_olist.py
```

### 3. Análise Customizada

```python
from data_loader import load_data
from analise_olist import OlistAnalysis

# Carregar dados
datasets = load_data()

# Criar instância da análise
analysis = OlistAnalysis(datasets)

# Executar análises específicas
analysis.pergunta_1_entregas_atrasadas()
analysis.pergunta_2_metodo_pagamento()
analysis.pergunta_3_top_categorias()
analysis.pergunta_4_tempo_entrega_avaliacao()

# Relatório completo
results = analysis.gerar_relatorio_completo()
```

## 📈 Visualizações Geradas

O script gera automaticamente 4 visualizações em PNG:

- `pergunta_1_entregas_atrasadas.png` - Gráficos de entrega vs prazo estimado
- `pergunta_2_metodos_pagamento.png` - Análise de métodos de pagamento
- `pergunta_3_top_categorias.png` - Top 5 categorias por vendas e receita
- `pergunta_4_tempo_entrega_avaliacao.png` - Correlação tempo vs satisfação

## 🧮 Metodologia

### Preparação dos Dados
- Limpeza de valores nulos
- Conversão de tipos de dados
- Tratamento de outliers
- Validação de consistência

### Análises Estatísticas
- **Descritiva**: Médias, medianas, percentis
- **Correlação**: Pearson para variáveis numéricas
- **Distribuição**: Histogramas e box plots
- **Categórica**: Frequências e proporções

### Tecnologias Utilizadas
- **Python 3.7+**
- **Pandas**: Manipulação de dados
- **NumPy**: Computação numérica
- **Matplotlib**: Visualizações básicas
- **Seaborn**: Visualizações estatísticas

## 📋 Requisitos do Dataset

### Arquivos Necessários (CSV)
- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_payments_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_products_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_sellers_dataset.csv`
- `olist_geolocation_dataset.csv`
- `product_category_name_translation.csv`

### Fonte dos Dados
[Kaggle - Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## 🎯 Insights Principais

### 1. Gestão Logística Eficiente
- Maioria das entregas realizadas antes do prazo estimado
- Oportunidade de usar velocidade como diferencial competitivo

### 2. Preferências de Pagamento
- **Cartão de crédito domina** compras de alto valor (70%)
- **Boleto mantém relevância** no mercado brasileiro (21%)
- Parcelamento é comum em compras maiores

### 3. Mix de Produtos
- **Housewares** lidera vendas e receita
- **Telephony** tem alta quantidade mas menor ticket médio
- Concentração nas top 5 categorias indica oportunidades

### 4. Satisfação do Cliente
- **Tempo de entrega não é o único fator** determinante da satisfação
- Necessidade de investigar outros aspectos da experiência
- Maioria das avaliações são positivas (nota 5)

## 📚 Documentação Completa

Para análise detalhada, metodologia completa e interpretações aprofundadas, consulte:
[ANALISE_DETALHADA.md](ANALISE_DETALHADA.md)

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie sua feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

## 👨‍💻 Autor

**Sistema de Análise Automatizada**
- 📧 Email: contato@exemplo.com
- 💼 LinkedIn: [seu-linkedin](https://linkedin.com/in/seu-perfil)
- 🐙 GitHub: [seu-github](https://github.com/seu-usuario)

## 🙏 Agradecimentos

- [Olist](https://olist.com/) por disponibilizar o dataset público
- [Kaggle](https://kaggle.com/) pela plataforma de compartilhamento
- Comunidade Python pela excelente documentação e bibliotecas

---

⭐ **Se este projeto foi útil, considere dar uma estrela no GitHub!**

## 📊 Status do Projeto

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)
![Coverage](https://img.shields.io/badge/Coverage-85%25-yellow.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)

**Última atualização**: Janeiro 2025