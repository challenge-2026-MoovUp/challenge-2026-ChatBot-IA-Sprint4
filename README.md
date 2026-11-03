# MoovUp — Sprint 4 | Inteligência Artificial e Machine Learning

## Sobre o projeto

O **MoovUp** é um projeto desenvolvido como parte do Challenge FIAP 2026. Nesta Sprint, o objetivo é aplicar técnicas de Inteligência Artificial e Machine Learning para analisar dados de usuários, identificar níveis de engajamento e realizar previsões de pontos acumulados.

O projeto utiliza uma base de dados com 500 usuários e desenvolve modelos de classificação e regressão.

## Objetivos

- Analisar a base de dados dos usuários.
- Desenvolver modelos de Machine Learning.
- Classificar usuários de acordo com seu nível de engajamento.
- Prever a quantidade de pontos acumulados.
- Avaliar o desempenho dos modelos.
- Disponibilizar modelos treinados para utilização futura.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Flask
- Joblib
- Jupyter Notebook

## Base de dados

A base utilizada contém 500 registros e 11 colunas, sem valores ausentes.

Entre as informações disponíveis estão:

- Idade
- Região
- Transporte principal
- Frequência de uso semanal
- Pontos acumulados
- Pontos resgatados
- Bilhetes resgatados
- Ações realizadas
- Pontuação e nível de engajamento

## Modelos desenvolvidos

### 1. Classificação — Random Forest

Responsável por classificar os usuários em três níveis de engajamento:

- Baixo
- Médio
- Alto

**Resultado obtido:**
- Acurácia: 82%

### 2. Regressão — Gradient Boosting

Responsável por estimar a quantidade de pontos acumulados pelos usuários.

Foram testadas diferentes configurações e algoritmos para encontrar o melhor resultado.

**Melhor resultado obtido:**
- MAE: 348,39
- RMSE: 407,49
- R²: -0,0477

O resultado indica limitações na capacidade de previsão do modelo, mostrando oportunidades de melhoria na seleção de variáveis e na qualidade dos dados.

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `MoovUp_Sprint4_Modelos.ipynb` | Notebook com análises, treinamento e avaliação |
| `base_moovup_500_usuarios.csv` | Base de dados utilizada |
| `base_moovup.xls` | Base original |
| `explicacoes.txt` | Explicações sobre os dados |
| `treinar_modelo.py` | Script de treinamento |
| `api_moovup.py` | API desenvolvida com Flask |
| `modelo_engajamento.joblib` | Modelo de classificação |
| `modelo_engajamento_notebook.joblib` | Modelo de classificação do notebook |
| `modelo_pontos.joblib` | Modelo de regressão original |
| `modelo_pontos_notebook.joblib` | Modelo de regressão do notebook |
| `modelo_pontos_gradient_boosting.joblib` | Melhor modelo de regressão testado |

## Como executar

### 1. Instalar as dependências

```bash
pip install pandas numpy scikit-learn matplotlib flask joblib xlrd
```

### 2. Executar o notebook

Abra o arquivo `MoovUp_Sprint4_Modelos.ipynb` no VS Code ou Jupyter Notebook e execute as células em ordem.

### 3. Executar a API

```bash
python api_moovup.py
```

A API será disponibilizada localmente em:

`http://127.0.0.1:5000`

## Integrantes

- Matheus Matsushita de Souza
- Pedro Amaro Pires
- Lucas Leite Carlos
- Juan Souza Marques

## Projeto acadêmico

Desenvolvido para o Challenge FIAP 2026 — Sprint 4.

**MoovUp | Artificial Intelligence & Chatbot**
