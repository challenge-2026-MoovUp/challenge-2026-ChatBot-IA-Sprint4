# MoovUp - IA para Predição de Engajamento

## Visão geral

Este projeto tem como objetivo desenvolver modelos de Machine Learning para prever o nível de engajamento dos usuários da plataforma MoovUp e estimar a quantidade de pontos acumulados com base em diferentes características de uso.

A solução inclui:

- treinamento de modelos de classificação para identificar o nível de engajamento;
- treinamento de modelo de regressão para estimar pontos acumulados;
- API em Flask para fornecer previsões em tempo real;
- notebook com análise exploratória e desenvolvimento dos modelos.

## Integrantes

- Matheus Matsushita de Souza - RM570017
- Pedro Amaro Pires - RM570636
- Lucas Leite Carlos - RM571985
- Juan Souza Marques - RM573469

## Objetivo da IA

A proposta é analisar o comportamento dos usuários com base em variáveis como idade, região, transporte principal, frequência de uso, pontos acumulados, pontos resgatados, bilhetes resgatados e ações realizadas, para classificar o nível de engajamento em:

- Baixo
- Médio
- Alto

Além disso, o projeto também estima a quantidade de pontos que um usuário pode acumular ao longo do tempo.

## Base de dados

A base utilizada foi criada sinteticamente para representar usuários fictícios da MoovUp. A base possui 500 registros e foi validada para verificar:

- ausência de dados vazios;
- ausência de registros duplicados;
- consistência das features utilizadas.

Principais colunas:

- id_usuario
- idade
- regiao
- transporte_principal
- frequencia_uso_semana
- pontos_acumulados
- pontos_resgatados
- bilhetes_resgatados
- acoes_realizadas
- pontuacao_engajamento
- nivel_engajamento

## Modelos utilizados

### 1. Modelo de classificação

Utiliza Random Forest Classifier para prever o nível de engajamento do usuário.

### 2. Modelo de regressão

Utiliza Random Forest Regressor para estimar a quantidade de pontos acumulados.

## Estrutura do projeto

```text
.
├── api_moovup.py                 # API Flask para previsão de engajamento
├── treinar_modelo.py            # Script responsável pelo treinamento dos modelos
├── MoovUp_Sprint4_Modelos.ipynb # Notebook com análise, treino e avaliação
├── base_moovup_500_usuarios.csv # Base de dados utilizada
├── modelo_engajamento.joblib    # Modelo treinado de classificação
├── modelo_pontos.joblib         # Modelo treinado de regressão
├── modelo_engajamento_notebook.joblib
├── modelo_pontos_notebook.joblib
├── modelo_pontos_gradient_boosting.joblib
├── explicacoes.txt              # Documentação e explicações do projeto
├── README.md                   # Documentação do repositório
└── .gitignore                  # Arquivos ignorados pelo Git
```

## Requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.10+
- pandas
- scikit-learn
- joblib
- Flask

Instalação das dependências:

```bash
pip install pandas scikit-learn joblib flask
```

## Como treinar os modelos

Execute o script:

```bash
python treinar_modelo.py
```

Esse script:

- carrega a base de dados;
- prepara as variáveis de entrada;
- treina o modelo de classificação;
- treina o modelo de regressão;
- salva os arquivos `.joblib` com os modelos e metadados.

## Como executar a API

Na raiz do projeto, rode:

```bash
python api_moovup.py
```

A API será iniciada em:

```text
http://127.0.0.1:5000
```

## Endpoints

### GET /

Retorna uma mensagem de confirmação do serviço.

### POST /predict

Recebe os dados do usuário em JSON e retorna o nível de engajamento previsto.

Exemplo de requisição:

```json
{
  "idade": 29,
  "regiao": "sul",
  "transporte_principal": "metro",
  "frequencia_uso_semana": 5,
  "pontos_acumulados": 150,
  "pontos_resgatados": 40,
  "bilhetes_resgatados": 2,
  "acoes_realizadas": 12,
  "pontuacao_engajamento": 80
}
```

Exemplo de resposta:

```json
{
  "projeto": "MoovUp",
  "nivel_engajamento_previsto": "Alto"
}
```

## Observações

- Os modelos foram treinados com dados sintéticos, então são adequados para demonstração e validação conceitual.
- O notebook pode ser usado para explorar a base, testar diferentes modelos e ajustar os hiperparâmetros.
- A API pode ser integrada a aplicações web, chatbots ou dashboards para tomada de decisão em tempo real.

## Resultado esperado

O projeto permite:

- identificar usuários com maior ou menor engajamento;
- segmentar clientes por comportamento;
- estimar pontos acumulados para ações de retenção e relacionamento;
- servir como base para futuras melhorias em recomendação e personalização.

---

Este projeto foi desenvolvido como parte do desafio de IA da Sprint 4 da MoovUp.
