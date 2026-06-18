import pandas as pd
import time
from datetime import datetime

agora = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

arquivo_excel = f'relatorio_{agora}.xlsx'


def dados(lista_produtos):
    
    
    
    df = pd.DataFrame(lista_produtos).drop_duplicates(subset=['Titulo Do Livro']).dropna()
    
    if df.empty:
        print("❌ Nenhum dado válido encontrado")
        return
    
    preco_medio = df['Preço Do Livro (£)'].mean()
    preco_mediano = df['Preço Do Livro (£)'].median()
    top_10_caros = df.nlargest(10, 'Preço Do Livro (£)')
    top_10_baratos = df.nsmallest(10, 'Preço Do Livro (£)')
    top_10_estoque = df.nlargest(10, 'Quantidade em Estoque')
    top_10_estrelas = df.nlargest(10, 'Estrelas')
    
    #relatorio terminal
    print('=' * 60)
    print('📊 Gerando relatório...')
    time.sleep(1)

    print('📚 Calculando métricas...')
    time.sleep(1)

    print('💰 Analisando preços...')
    time.sleep(1)

    print('📄 Preparando relatório...')
    time.sleep(1)
    
    print('=' * 60)
    print('📊 RESUMO GERAL')
    print(f'📚 LIVROS ANALISADOS : {len(df)}')
    print(f'💰 PREÇO MÉDIO : {preco_medio:.2f}')
    print(f'📍 PREÇO MEDIANO : {preco_mediano:.2f}')
    print('=' * 60)
    print('🏆 TOP 10 LIVROS MAIS CAROS :\n')
    print(top_10_caros[['Titulo Do Livro', 'Preço Do Livro (£)']].to_string(index=False))
    print('=' * 60)
    print('💸 TOP 10 LIVROS MAIS BARATOS :\n')
    print(top_10_baratos[['Titulo Do Livro', 'Preço Do Livro (£)']].to_string(index=False))
    print('=' * 60)
    print('📦 TOP 10 MAIORES ESTOQUES :\n')
    print(top_10_estoque[['Titulo Do Livro', 'Quantidade em Estoque']].to_string(index=False))
    print('=' * 60)
    print('⭐ TOP 10 LIVROS MAIS BEM AVALIADOS :\n')
    print(top_10_estrelas[['Titulo Do Livro', 'Estrelas']].to_string(index=False))
    print('=' * 60)
    
    time.sleep(1)
    print('✅ Relatório concluído!')
    
    resumo = pd.DataFrame({
    'Métrica': [
        'Livros Analisados',
        'Preço Médio',
        'Preço Mediano'
    ],
    'Valor': [
        len(df),
        round(preco_medio, 2),
        round(preco_mediano, 2)
    ]})
    
    with pd.ExcelWriter(arquivo_excel, engine="openpyxl") as writer:
        resumo.to_excel(writer, sheet_name='RESUMO GERAL', index=False)
        df.to_excel(writer, sheet_name='LIVROS', index=False)
        top_10_caros.to_excel(writer, sheet_name='TOP 10 LIVROS MAIS CAROS', index=False)
        top_10_baratos.to_excel(writer, sheet_name='TOP 10 LIVROS MAIS BARATOS', index=False)
        top_10_estoque.to_excel(writer, sheet_name='TOP 10 MAIORES ESTOQUES', index=False)
        top_10_estrelas.to_excel(writer, sheet_name='TOP 10 LIVROS MAIS BEM AVALIADOS', index=False)
