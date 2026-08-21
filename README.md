# 📊 Dashboard de Análise de Vendas de Notebooks

Aplicação web interativa desenvolvida em Python para análise comparativa do mercado de notebooks vendidos no Mercado Livre, oferecendo visualização gráfica interativa, controle de filtros e exportação de relatórios.

---

## 🚀 Funcionalidades

- **Filtros Dinâmicos:** Seleção por marcas (fabricantes) e intervalo de quantidades vendidas na barra lateral.
- **Métricas em Destaque:** Visualização de Receita Total Bruta, Média de Receita e Destaque para o Produto Mais Vendido.
- **Gráficos Interativos (Plotly):**
  - Receita total por fabricante (Gráfico de Barras).
  - Média de receita por fabricante (Gráfico de Linhas).
- **Abas de Organização:**
  - Aba com gráficos interativos.
  - Aba com ranking das empresas TOP ONE e exibição da base de dados.
- **Exportação de Dados:** Botão para download direto dos dados filtrados em formato `.csv`.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit** (Interface gráfica do Dashboard)
- **Pandas** (Tratamento e manipulação de dados)
- **Plotly** (Visualização gráfica interativa)
- **OpenPyXL** (Leitura de planilhas Excel)

---

## 📁 Estrutura do Projeto

```text
├── Analise.py         # Código da aplicação Streamlit
├── Dados.xlsx         # Base de dados do projeto
├── .gitignore         # Configuração de arquivos ignorados pelo Git
└── README.md          # Documentação do projeto
