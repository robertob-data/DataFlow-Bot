# 🕷️ Web Scraper

---

## 📌 Descrição do projeto

Este projeto é um sistema automatizado em Python que realiza scraping de livros em um site, coleta informações como preço, avaliação e estoque, e gera relatórios analíticos completos em Excel.

Ele resolve o problema de coleta manual e análise demorada de catálogos, transformando páginas web em dados estruturados e insights rápidos.

---

## 🚧 Status do projeto

🟢 Finalizado (versão funcional de estudo e portfólio)

---

## ⚙️ Funcionalidades

- Coleta automática de livros em múltiplas páginas
- Extração de:
  - Título do livro
  - Preço
  - Avaliação (estrelas)
  - Quantidade em estoque
- Limpeza e estruturação de dados com Pandas
- Cálculo de métricas:
  - Preço médio
  - Preço mediano
- Rankings automáticos:
  - Livros mais caros
  - Livros mais baratos
  - Maior estoque
  - Melhores avaliados
- Geração de relatório em Excel com múltiplas abas
- Logs de execução no terminal

---

## 🧠 Tecnologias utilizadas

- Python
- BeautifulSoup (bs4)
- Requests
- Pandas
- OpenPyXL

---

## 📦 Pré-requisitos

- Python 3.10 ou superior recomendado

## 🚀 Passo a passo de instalação

```bash
# clonar o repositório
git clone https://github.com/seu-usuario/seu-repo.git

# entrar na pasta
cd seu-repo

# criar ambiente virtual (opcional)
python -m venv venv

# ativar ambiente virtual (Windows)
venv\Scripts\activate

# instalar dependências
pip install requests beautifulsoup4 pandas openpyxl
```

## ▶️ Instruções de execução

```bash
python main.py
```

## 📁 Estrutura de arquivos

```text
📦 projeto
 ┣ 📜 main.py
 ┣ 📜 scrapper.py
 ┣ 📜 analize_persist.py
```

## 📊 Exemplo de saída

```text
📊 RESUMO GERAL
📚 LIVROS ANALISADOS: 40
💰 PREÇO MÉDIO: 34.52
📍 PREÇO MEDIANO: 29.90

🏆 TOP 10 LIVROS MAIS CAROS
- Livro X — £59.99
- Livro Y — £55.20
```

## 📄 Licença

MIT License — uso livre para fins educacionais e pessoais.

## 👤 Autoria

Desenvolvido por Roberto Batista Dias
