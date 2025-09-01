#!/usr/bin/env python3
"""
Script de instalação e execução da análise Olist
"""

import subprocess
import sys
import os

def install_requirements():
    """Instalar dependências necessárias"""
    print("Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar dependências")
        return False

def run_analysis():
    """Executar a análise"""
    print("Executando análise...")
    try:
        subprocess.check_call([sys.executable, "analise_olist.py"])
        print("✅ Análise concluída com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao executar análise")
        return False

def main():
    print("🚀 Setup da Análise de Dados Olist")
    print("=" * 50)
    
    # Verificar se requirements.txt existe
    if not os.path.exists("requirements.txt"):
        print("❌ Arquivo requirements.txt não encontrado")
        return
    
    # Instalar dependências
    if not install_requirements():
        return
    
    print("\n" + "=" * 50)
    
    # Executar análise
    if not run_analysis():
        return
    
    print("\n🎉 Processo concluído!")
    print("📊 Verifique os gráficos gerados:")
    print("  - pergunta_1_entregas_atrasadas.png")
    print("  - pergunta_2_metodos_pagamento.png")
    print("  - pergunta_3_top_categorias.png")
    print("  - pergunta_4_tempo_entrega_avaliacao.png")
    print("\n📋 Para análise detalhada, consulte: ANALISE_DETALHADA.md")

if __name__ == "__main__":
    main()