# 📊 Inteligência de Vendas - Mercado Livre

![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

Um dashboard interativo e dinâmico desenvolvido em Python para análise de performance de vendas das principais marcas de notebooks no Mercado Livre. O projeto permite a visualização de Indicadores Chave de Performance (KPIs), Market Share e distribuição de receita através de gráficos interativos.

## ✨ Funcionalidades

*   **Resumo de KPIs (Cartões Visuais):** Acompanhamento rápido do total de marcas, receita bruta total, ticket médio e maior venda registrada.
*   **Filtros Dinâmicos:** Filtro multiseleção por fabricante e barra deslizante (slider) para filtrar a faixa de receita (TOTAL).
*   **Gráficos Interativos (Plotly):** 
    *   Gráfico de Barras: Top faturamento por marca.
    *   Gráfico de Rosca: Market Share (Fatia de Mercado).
    *   Boxplot: Distribuição de valores de receita por marca.
*   **Exportação de Dados:** Tabela de dados brutos com botão para download imediato em formato `.csv`.
*   **Design Responsivo:** Interface em modo escuro (Dark Mode) focada na experiência do usuário (UX).

## 🚀 Tecnologias Utilizadas

*   [Python](https://www.python.org/) - Linguagem principal.
*   [Streamlit](https://streamlit.io/) - Framework para criação da interface web (Front-end).
*   [Pandas](https://pandas.pydata.org/) - Manipulação e análise de dados.
*   [Plotly](https://plotly.com/python/) - Criação de gráficos interativos.
*   [Openpyxl](https://openpyxl.readthedocs.io/en/stable/) - Leitura de planilhas Excel (`.xlsx`).

## 📁 Estrutura do Projeto

```text
├── app.py                # Script principal da aplicação Streamlit
├── Dados.xlsx            # Base de dados utilizada no dashboard
├── requirements.txt      # Lista de dependências do projeto
├── .gitignore            # Arquivos e pastas ignorados pelo Git (.venv, __pycache__, etc)
└── README.md             # Documentação do projeto
🛠️ Como Executar o Projeto Localmente
Pré-requisitos: É necessário ter o Python instalado na sua máquina (versão 3.8 ou superior recomendada).

1. Clone o repositório

Bash
git clone https://github.com/Bottino16/Analise-de-Dados-em-Python.git
cd NOME-DO-SEU-REPOSITORIO
2. Crie e ative um ambiente virtual (Opcional, mas recomendado)

Bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual (Windows)
.venv\Scripts\activate

# Ativar ambiente virtual (Linux/Mac)
source .venv/bin/activate
3. Instale as dependências

Bash
pip install -r requirements.txt
4. Execute a aplicação

Bash
streamlit run app.py
O servidor será iniciado e o dashboard abrirá automaticamente no seu navegador padrão (geralmente em http://localhost:8501).

Autor: Felipe Bottino (Wallace Oliveira)


### O que você pode personalizar depois:
*   **Link do `git clone`**: Substitua `NOME-DO-SEU-REPOSITORIO` pelo nome real que você deu ao repositório no GitHub.
*   **Imagens**: Você pode tirar um *Print Screen* da tela do seu Dashboard pronto, salvar como `print.png`, colocar na pasta do projeto e adicionar o código `![Dashboard](print.png)` logo abaixo do título no README para que as pessoas vejam a cara do projeto antes mesmo de rodar!

Se quiser adicionar esse arquivo ao GitHub agora, basta criar o arquivo localmente e usar os comandos `git add README.md`, `git commit -m "Add README"` e `git push`.
