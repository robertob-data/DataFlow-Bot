from scrapper import scraper
from analize_persist import dados
import time

inicio = time.time()

print("=" * 60)
print("🤖 SISTEMA DE SCRAPING + ANÁLISE DE LIVROS")
print("📊 Geração automática de relatórios em Excel")
print("=" * 60)
print("\n📌 Etapas do processo:")
print("1. Coleta de dados")
print("2. Análise estatística")
print("3. Geração de relatório")
print("4. Exportação em Excel")

while True:
    try:
        paginas = input("\n📥 Quantas páginas deseja analisar? (1/50) ")
        paginas = int(paginas)
        if paginas > 0 and paginas <= 50:
            break
        else:
            print('\n❗ Escolha um numero de 1 a 50!!')
    except Exception as e:
        print('\n❗ Por favor, digite apenas numeros inteiros')
    

print("\n🔄 Iniciando coleta de dados...")
time.sleep(1)
print("📡 Coletando páginas...")
print("⏳ Isso pode levar alguns segundos...")
livros = scraper(paginas)
print("📊 Processando dados...")
dados(livros)
print("📁 Arquivos gerados com sucesso.")
print(f"📚 Total de livros coletados: {len(livros)}")
print(f"📄 Páginas analisadas: {paginas}")
print("\n🎉 PROCESSO FINALIZADO COM SUCESSO!")
print("📁 Arquivos gerados com sucesso.")
fim = time.time()

print(f"\n⏱️ Tempo total de execução: {fim - inicio:.2f} segundos")

input("\n👉 Pressione ENTER para encerrar o sistema...")