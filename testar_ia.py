
import joblib
import pandas as pd

# Carregar o modelo treinado
modelo = joblib.load("modelo_engajamento_notebook.joblib")

# Criar os dados do usuário
usuario = pd.DataFrame([{
    "idade": 22,
    "frequencia_uso_semana": 5,
    "pontos_resgatados": 200,
    "bilhetes_resgatados": 3,
    "acoes_realizadas": 10,
    "regiao_Sul": 0,
    "regiao_Oeste": 0,
    "regiao_Leste": 0,
    "regiao_Norte": 0,
    "transporte_principal_Trem": 0,
    "transporte_principal_Onibus": 1
}])

# Fazer a previsão
previsao = modelo.predict(usuario)

print("===== MOOVUP AI =====")
print("Idade:", 22)
print("Frequência semanal:", 5)
print("Ações realizadas:", 10)
print("Engajamento previsto:", previsao[0])
