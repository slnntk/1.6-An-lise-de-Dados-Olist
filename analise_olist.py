#!/usr/bin/env python3
"""
Análise de Dados Olist - Brazilian E-Commerce Dataset

Este script responde às 4 perguntas principais sobre o dataset do Olist:
1. Qual o percentual de pedidos entregues após a data estimada pela Olist?
2. Qual o método de pagamento mais utilizado em pedidos acima de R$ 150,00?
3. Quais são as 5 categorias de produtos mais vendidas e qual a receita total gerada por cada uma?
4. Qual é a relação entre o tempo de entrega e a nota de avaliação do cliente?
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuração para visualizações
plt.style.use('default')
sns.set_palette("husl")

def setup_matplotlib():
    """Configurar matplotlib para visualizações"""
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['ytick.labelsize'] = 8

class OlistAnalysis:
    def __init__(self, datasets):
        """
        Inicializa a análise com os datasets do Olist
        
        Parameters:
        datasets (dict): Dicionário contendo todos os datasets
        """
        self.datasets = datasets
        self.results = {}
        self.prepare_data()
    
    def prepare_data(self):
        """Preparar e limpar os dados para análise"""
        print("Preparando dados para análise...")
        
        # Converter colunas de data para datetime
        date_columns = {
            'orders': ['order_purchase_timestamp', 'order_approved_at', 
                      'order_delivered_carrier_date', 'order_delivered_customer_date', 
                      'order_estimated_delivery_date'],
            'order_reviews': ['review_creation_date', 'review_answer_timestamp'],
            'order_items': ['shipping_limit_date']
        }
        
        for dataset_name, cols in date_columns.items():
            if dataset_name in self.datasets:
                for col in cols:
                    if col in self.datasets[dataset_name].columns:
                        self.datasets[dataset_name][col] = pd.to_datetime(
                            self.datasets[dataset_name][col], errors='coerce'
                        )
        
        print("Dados preparados com sucesso!")
    
    def pergunta_1_entregas_atrasadas(self):
        """
        Pergunta 1: Qual o percentual de pedidos entregues após a data estimada pela Olist?
        """
        print("\n" + "="*70)
        print("PERGUNTA 1: Percentual de pedidos entregues após a data estimada")
        print("="*70)
        
        orders = self.datasets['orders'].copy()
        
        # Filtrar pedidos entregues e com datas válidas
        delivered_orders = orders[
            (orders['order_status'] == 'delivered') &
            (orders['order_delivered_customer_date'].notna()) &
            (orders['order_estimated_delivery_date'].notna())
        ].copy()
        
        if len(delivered_orders) == 0:
            print("Não há dados suficientes para análise de entregas.")
            return
        
        # Calcular atraso
        delivered_orders['atraso_dias'] = (
            delivered_orders['order_delivered_customer_date'] - 
            delivered_orders['order_estimated_delivery_date']
        ).dt.days
        
        # Classificar entregas
        delivered_orders['status_entrega'] = delivered_orders['atraso_dias'].apply(
            lambda x: 'Atrasado' if x > 0 else 'No Prazo' if x == 0 else 'Antecipado'
        )
        
        # Calcular estatísticas
        total_entregas = len(delivered_orders)
        entregas_atrasadas = len(delivered_orders[delivered_orders['atraso_dias'] > 0])
        entregas_no_prazo = len(delivered_orders[delivered_orders['atraso_dias'] == 0])
        entregas_antecipadas = len(delivered_orders[delivered_orders['atraso_dias'] < 0])
        
        percentual_atraso = (entregas_atrasadas / total_entregas) * 100
        percentual_no_prazo = (entregas_no_prazo / total_entregas) * 100
        percentual_antecipado = (entregas_antecipadas / total_entregas) * 100
        
        # Salvar resultados
        self.results['pergunta_1'] = {
            'total_entregas': total_entregas,
            'entregas_atrasadas': entregas_atrasadas,
            'percentual_atraso': percentual_atraso,
            'percentual_no_prazo': percentual_no_prazo,
            'percentual_antecipado': percentual_antecipado,
            'atraso_medio_dias': delivered_orders[delivered_orders['atraso_dias'] > 0]['atraso_dias'].mean()
        }
        
        # Apresentar resultados
        print(f"Total de entregas analisadas: {total_entregas:,}")
        print(f"Entregas atrasadas: {entregas_atrasadas:,} ({percentual_atraso:.2f}%)")
        print(f"Entregas no prazo: {entregas_no_prazo:,} ({percentual_no_prazo:.2f}%)")
        print(f"Entregas antecipadas: {entregas_antecipadas:,} ({percentual_antecipado:.2f}%)")
        
        if entregas_atrasadas > 0:
            atraso_medio = delivered_orders[delivered_orders['atraso_dias'] > 0]['atraso_dias'].mean()
            print(f"Atraso médio: {atraso_medio:.1f} dias")
        
        # Criar visualização
        plt.figure(figsize=(10, 6))
        
        # Gráfico de pizza
        plt.subplot(1, 2, 1)
        labels = ['Atrasado', 'No Prazo', 'Antecipado']
        sizes = [percentual_atraso, percentual_no_prazo, percentual_antecipado]
        colors = ['#ff9999', '#66b3ff', '#99ff99']
        
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title('Distribuição do Status de Entrega')
        
        # Histograma de atrasos
        plt.subplot(1, 2, 2)
        atrasos = delivered_orders['atraso_dias']
        plt.hist(atrasos, bins=30, color='skyblue', alpha=0.7, edgecolor='black')
        plt.axvline(x=0, color='red', linestyle='--', label='Data Estimada')
        plt.xlabel('Dias de Atraso/Antecipação')
        plt.ylabel('Número de Pedidos')
        plt.title('Distribuição de Atrasos/Antecipações')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('pergunta_1_entregas_atrasadas.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return self.results['pergunta_1']
    
    def pergunta_2_metodo_pagamento(self):
        """
        Pergunta 2: Qual o método de pagamento mais utilizado em pedidos acima de R$ 150,00?
        """
        print("\n" + "="*70)
        print("PERGUNTA 2: Método de pagamento mais usado em pedidos > R$ 150,00")
        print("="*70)
        
        payments = self.datasets['order_payments'].copy()
        
        # Filtrar pedidos acima de R$ 150,00
        payments_above_150 = payments[payments['payment_value'] > 150.0]
        
        if len(payments_above_150) == 0:
            print("Não há pedidos acima de R$ 150,00 no dataset.")
            return
        
        # Agrupar por método de pagamento
        payment_stats = payments_above_150.groupby('payment_type').agg({
            'order_id': 'count',
            'payment_value': ['sum', 'mean']
        }).round(2)
        
        payment_stats.columns = ['quantidade_pedidos', 'valor_total', 'valor_medio']
        payment_stats['percentual'] = (payment_stats['quantidade_pedidos'] / payment_stats['quantidade_pedidos'].sum()) * 100
        payment_stats = payment_stats.sort_values('quantidade_pedidos', ascending=False)
        
        # Salvar resultados
        self.results['pergunta_2'] = {
            'total_pedidos_acima_150': len(payments_above_150),
            'metodo_mais_usado': payment_stats.index[0],
            'percentual_metodo_principal': payment_stats.iloc[0]['percentual'],
            'payment_stats': payment_stats
        }
        
        # Apresentar resultados
        print(f"Total de pedidos acima de R$ 150,00: {len(payments_above_150):,}")
        print(f"\nMétodo de pagamento mais utilizado: {payment_stats.index[0]}")
        print(f"Representa {payment_stats.iloc[0]['percentual']:.2f}% dos pedidos acima de R$ 150,00")
        print(f"\nEstatísticas por método de pagamento:")
        print(payment_stats)
        
        # Criar visualização
        plt.figure(figsize=(12, 6))
        
        # Gráfico de barras - Quantidade de pedidos
        plt.subplot(1, 2, 1)
        bars1 = plt.bar(payment_stats.index, payment_stats['quantidade_pedidos'], 
                       color='lightblue', edgecolor='black')
        plt.title('Quantidade de Pedidos > R$ 150 por Método de Pagamento')
        plt.xlabel('Método de Pagamento')
        plt.ylabel('Quantidade de Pedidos')
        plt.xticks(rotation=45)
        
        # Adicionar valores nas barras
        for bar in bars1:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{int(height)}', ha='center', va='bottom')
        
        # Gráfico de pizza - Percentual
        plt.subplot(1, 2, 2)
        plt.pie(payment_stats['percentual'], labels=payment_stats.index, 
                autopct='%1.1f%%', startangle=90)
        plt.title('Distribuição Percentual por Método de Pagamento')
        
        plt.tight_layout()
        plt.savefig('pergunta_2_metodos_pagamento.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return self.results['pergunta_2']
    
    def pergunta_3_top_categorias(self):
        """
        Pergunta 3: Quais são as 5 categorias de produtos mais vendidas e qual a receita total gerada por cada uma?
        """
        print("\n" + "="*70)
        print("PERGUNTA 3: Top 5 categorias de produtos mais vendidas e receita")
        print("="*70)
        
        order_items = self.datasets['order_items'].copy()
        products = self.datasets['products'].copy()
        
        # Merge dos dados
        items_products = order_items.merge(products, on='product_id', how='left')
        
        # Remover linhas onde category é nulo
        items_products = items_products.dropna(subset=['product_category_name'])
        
        if len(items_products) == 0:
            print("Não há dados de produtos com categorias para análise.")
            return
        
        # Agrupar por categoria
        category_stats = items_products.groupby('product_category_name').agg({
            'order_id': 'count',  # Quantidade vendida
            'price': 'sum'        # Receita total
        }).round(2)
        
        category_stats.columns = ['quantidade_vendida', 'receita_total']
        category_stats = category_stats.sort_values('quantidade_vendida', ascending=False)
        
        # Top 5 categorias
        top_5_categories = category_stats.head(5)
        
        # Traduzir nomes se disponível
        if 'category_translation' in self.datasets:
            translation = self.datasets['category_translation'].set_index('product_category_name')
            top_5_categories_translated = top_5_categories.copy()
            
            for idx in top_5_categories.index:
                if idx in translation.index:
                    new_name = translation.loc[idx, 'product_category_name_english']
                    top_5_categories_translated = top_5_categories_translated.rename(index={idx: new_name})
        else:
            top_5_categories_translated = top_5_categories
        
        # Salvar resultados
        self.results['pergunta_3'] = {
            'top_5_categories': top_5_categories,
            'total_receita_top_5': top_5_categories['receita_total'].sum(),
            'total_vendas_top_5': top_5_categories['quantidade_vendida'].sum()
        }
        
        # Apresentar resultados
        print("Top 5 categorias de produtos mais vendidas:")
        print("-" * 50)
        for i, (categoria, dados) in enumerate(top_5_categories.iterrows(), 1):
            print(f"{i}. {categoria}")
            print(f"   Quantidade vendida: {dados['quantidade_vendida']:,}")
            print(f"   Receita total: R$ {dados['receita_total']:,.2f}")
            print()
        
        # Criar visualização
        plt.figure(figsize=(14, 10))
        
        # Gráfico de barras - Quantidade vendida
        plt.subplot(2, 2, 1)
        bars1 = plt.bar(range(5), top_5_categories['quantidade_vendida'], 
                       color='lightcoral', edgecolor='black')
        plt.title('Top 5 Categorias - Quantidade Vendida')
        plt.xlabel('Categoria')
        plt.ylabel('Quantidade Vendida')
        plt.xticks(range(5), [cat[:15] + '...' if len(cat) > 15 else cat 
                             for cat in top_5_categories.index], rotation=45)
        
        # Adicionar valores nas barras
        for i, bar in enumerate(bars1):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'{int(height):,}', ha='center', va='bottom', fontsize=8)
        
        # Gráfico de barras - Receita total
        plt.subplot(2, 2, 2)
        bars2 = plt.bar(range(5), top_5_categories['receita_total'], 
                       color='lightgreen', edgecolor='black')
        plt.title('Top 5 Categorias - Receita Total')
        plt.xlabel('Categoria')
        plt.ylabel('Receita Total (R$)')
        plt.xticks(range(5), [cat[:15] + '...' if len(cat) > 15 else cat 
                             for cat in top_5_categories.index], rotation=45)
        
        # Adicionar valores nas barras
        for i, bar in enumerate(bars2):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'R${height/1000:.0f}k', ha='center', va='bottom', fontsize=8)
        
        # Gráfico de pizza - Quantidade
        plt.subplot(2, 2, 3)
        plt.pie(top_5_categories['quantidade_vendida'], 
                labels=[cat[:20] + '...' if len(cat) > 20 else cat 
                       for cat in top_5_categories.index],
                autopct='%1.1f%%', startangle=90)
        plt.title('Distribuição de Vendas por Categoria')
        
        # Gráfico de pizza - Receita
        plt.subplot(2, 2, 4)
        plt.pie(top_5_categories['receita_total'], 
                labels=[cat[:20] + '...' if len(cat) > 20 else cat 
                       for cat in top_5_categories.index],
                autopct='%1.1f%%', startangle=90)
        plt.title('Distribuição de Receita por Categoria')
        
        plt.tight_layout()
        plt.savefig('pergunta_3_top_categorias.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return self.results['pergunta_3']
    
    def pergunta_4_tempo_entrega_avaliacao(self):
        """
        Pergunta 4: Qual é a relação entre o tempo de entrega e a nota de avaliação do cliente?
        """
        print("\n" + "="*70)
        print("PERGUNTA 4: Relação entre tempo de entrega e avaliação do cliente")
        print("="*70)
        
        orders = self.datasets['orders'].copy()
        reviews = self.datasets['order_reviews'].copy()
        
        # Merge entre pedidos e avaliações
        orders_reviews = orders.merge(reviews, on='order_id', how='inner')
        
        # Filtrar apenas pedidos entregues com datas válidas
        delivered_reviews = orders_reviews[
            (orders_reviews['order_status'] == 'delivered') &
            (orders_reviews['order_delivered_customer_date'].notna()) &
            (orders_reviews['order_purchase_timestamp'].notna()) &
            (orders_reviews['review_score'].notna())
        ].copy()
        
        if len(delivered_reviews) == 0:
            print("Não há dados suficientes para análise de tempo de entrega vs avaliação.")
            return
        
        # Calcular tempo de entrega em dias
        delivered_reviews['tempo_entrega_dias'] = (
            delivered_reviews['order_delivered_customer_date'] - 
            delivered_reviews['order_purchase_timestamp']
        ).dt.days
        
        # Remover outliers extremos (tempo de entrega negativo ou muito alto)
        delivered_reviews = delivered_reviews[
            (delivered_reviews['tempo_entrega_dias'] >= 0) & 
            (delivered_reviews['tempo_entrega_dias'] <= 100)
        ]
        
        if len(delivered_reviews) == 0:
            print("Não há dados válidos após remoção de outliers.")
            return
        
        # Calcular estatísticas por nota de avaliação
        stats_by_score = delivered_reviews.groupby('review_score')['tempo_entrega_dias'].agg([
            'count', 'mean', 'median', 'std'
        ]).round(2)
        
        # Calcular correlação
        correlation = delivered_reviews['tempo_entrega_dias'].corr(delivered_reviews['review_score'])
        
        # Salvar resultados
        self.results['pergunta_4'] = {
            'total_avaliacoes': len(delivered_reviews),
            'correlacao': correlation,
            'stats_by_score': stats_by_score,
            'tempo_medio_geral': delivered_reviews['tempo_entrega_dias'].mean()
        }
        
        # Apresentar resultados
        print(f"Total de avaliações analisadas: {len(delivered_reviews):,}")
        print(f"Correlação entre tempo de entrega e nota: {correlation:.3f}")
        print(f"Tempo médio de entrega: {delivered_reviews['tempo_entrega_dias'].mean():.1f} dias")
        print(f"\nEstatísticas por nota de avaliação:")
        print(stats_by_score)
        
        # Interpretação da correlação
        if correlation < -0.3:
            interpretacao = "Correlação negativa moderada: maior tempo de entrega tende a resultar em notas menores"
        elif correlation < -0.1:
            interpretacao = "Correlação negativa fraca: há uma leve tendência de notas menores com maior tempo de entrega"
        elif correlation > 0.1:
            interpretacao = "Correlação positiva fraca: maior tempo de entrega pode resultar em notas ligeiramente maiores"
        else:
            interpretacao = "Correlação muito fraca: não há relação clara entre tempo de entrega e nota"
        
        print(f"\nInterpretação: {interpretacao}")
        
        # Criar visualização
        plt.figure(figsize=(15, 10))
        
        # Scatter plot
        plt.subplot(2, 3, 1)
        plt.scatter(delivered_reviews['tempo_entrega_dias'], delivered_reviews['review_score'], 
                   alpha=0.5, color='blue')
        plt.xlabel('Tempo de Entrega (dias)')
        plt.ylabel('Nota de Avaliação')
        plt.title(f'Relação Tempo de Entrega vs Avaliação\n(Correlação: {correlation:.3f})')
        plt.grid(True, alpha=0.3)
        
        # Boxplot por nota
        plt.subplot(2, 3, 2)
        box_data = [delivered_reviews[delivered_reviews['review_score'] == score]['tempo_entrega_dias'] 
                   for score in sorted(delivered_reviews['review_score'].unique())]
        plt.boxplot(box_data, labels=sorted(delivered_reviews['review_score'].unique()))
        plt.xlabel('Nota de Avaliação')
        plt.ylabel('Tempo de Entrega (dias)')
        plt.title('Distribuição do Tempo de Entrega por Nota')
        plt.grid(True, alpha=0.3)
        
        # Tempo médio por nota
        plt.subplot(2, 3, 3)
        avg_time_by_score = delivered_reviews.groupby('review_score')['tempo_entrega_dias'].mean()
        bars = plt.bar(avg_time_by_score.index, avg_time_by_score.values, 
                      color='lightblue', edgecolor='black')
        plt.xlabel('Nota de Avaliação')
        plt.ylabel('Tempo Médio de Entrega (dias)')
        plt.title('Tempo Médio de Entrega por Nota')
        plt.grid(True, alpha=0.3)
        
        # Adicionar valores nas barras
        for bar, value in zip(bars, avg_time_by_score.values):
            plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
                    f'{value:.1f}', ha='center', va='bottom')
        
        # Histograma de tempo de entrega
        plt.subplot(2, 3, 4)
        plt.hist(delivered_reviews['tempo_entrega_dias'], bins=30, 
                color='skyblue', alpha=0.7, edgecolor='black')
        plt.xlabel('Tempo de Entrega (dias)')
        plt.ylabel('Frequência')
        plt.title('Distribuição do Tempo de Entrega')
        plt.grid(True, alpha=0.3)
        
        # Histograma de notas
        plt.subplot(2, 3, 5)
        plt.hist(delivered_reviews['review_score'], bins=5, 
                color='lightgreen', alpha=0.7, edgecolor='black')
        plt.xlabel('Nota de Avaliação')
        plt.ylabel('Frequência')
        plt.title('Distribuição das Notas de Avaliação')
        plt.grid(True, alpha=0.3)
        
        # Heatmap de correlação (se houver mais variáveis)
        plt.subplot(2, 3, 6)
        corr_data = delivered_reviews[['tempo_entrega_dias', 'review_score']].corr()
        sns.heatmap(corr_data, annot=True, cmap='coolwarm', center=0,
                   square=True, cbar_kws={'shrink': .8})
        plt.title('Matriz de Correlação')
        
        plt.tight_layout()
        plt.savefig('pergunta_4_tempo_entrega_avaliacao.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return self.results['pergunta_4']
    
    def gerar_relatorio_completo(self):
        """Gerar relatório completo da análise"""
        print("\n" + "="*70)
        print("RELATÓRIO COMPLETO - ANÁLISE DOS DADOS OLIST")
        print("="*70)
        
        # Resumo dos datasets
        print("\n1. RESUMO DOS DATASETS:")
        print("-" * 30)
        for name, df in self.datasets.items():
            print(f"{name}: {df.shape[0]:,} linhas, {df.shape[1]} colunas")
        
        # Resumo das respostas
        print(f"\n2. RESUMO DAS RESPOSTAS:")
        print("-" * 30)
        
        if 'pergunta_1' in self.results:
            result = self.results['pergunta_1']
            print(f"Pergunta 1: {result['percentual_atraso']:.2f}% dos pedidos foram entregues com atraso")
        
        if 'pergunta_2' in self.results:
            result = self.results['pergunta_2']
            print(f"Pergunta 2: {result['metodo_mais_usado']} é o método mais usado em pedidos > R$ 150")
        
        if 'pergunta_3' in self.results:
            result = self.results['pergunta_3']
            top_category = result['top_5_categories'].index[0]
            print(f"Pergunta 3: {top_category} é a categoria mais vendida")
        
        if 'pergunta_4' in self.results:
            result = self.results['pergunta_4']
            print(f"Pergunta 4: Correlação tempo-avaliação = {result['correlacao']:.3f}")
        
        print(f"\n3. ARQUIVOS GERADOS:")
        print("-" * 20)
        print("- pergunta_1_entregas_atrasadas.png")
        print("- pergunta_2_metodos_pagamento.png") 
        print("- pergunta_3_top_categorias.png")
        print("- pergunta_4_tempo_entrega_avaliacao.png")
        
        return self.results

def main():
    """Função principal"""
    print("ANÁLISE DE DADOS OLIST - BRAZILIAN E-COMMERCE DATASET")
    print("=" * 60)
    
    # Configurar matplotlib
    setup_matplotlib()
    
    # Carregar dados
    try:
        from data_loader import load_data
        datasets = load_data()
    except ImportError:
        print("Erro: não foi possível importar data_loader")
        return
    
    if not datasets:
        print("Erro: não foi possível carregar os datasets")
        return
    
    # Criar instância da análise
    analysis = OlistAnalysis(datasets)
    
    # Executar todas as análises
    print("\nIniciando análise...")
    
    try:
        analysis.pergunta_1_entregas_atrasadas()
        analysis.pergunta_2_metodo_pagamento()
        analysis.pergunta_3_top_categorias()
        analysis.pergunta_4_tempo_entrega_avaliacao()
        
        # Gerar relatório final
        analysis.gerar_relatorio_completo()
        
        print(f"\nAnálise concluída com sucesso!")
        print("Verifique os gráficos gerados em formato PNG.")
        
    except Exception as e:
        print(f"Erro durante a análise: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()