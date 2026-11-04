import joblib
import pandas as pd
import joblib
import pandas as pd

modelo = joblib.load("modelo_engajamento_notebook.joblib")

print("===== MOOVUP AI =====")
print("Vamos analisar o engajamento de um usuário!\n")

idade = int(input("Digite a idade: "))
frequencia = int(input("Usos por semana: "))
pontos = int(input("Pontos acumulados: "))
pontos_resgatados = int(input("Pontos resgatados: "))
bilhetes = int(input("Bilhetes resgatados: "))
acoes = int(input("Ações realizadas: "))

dados = {
    "idade": idade,
    "frequencia_uso_semana": frequencia,
    "pontos_acumulados": pontos,
    "pontos_resgatados": pontos_resgatados,
    "bilhetes_resgatados": bilhetes,
    "acoes_realizadas": acoes,
    "regiao_Sul": 0,
    "regiao_Oeste": 0,
    "regiao_Leste": 0,
    "regiao_Norte": 0,
    "transporte_principal_Trem": 0,
    "transporte_principal_Onibus": 1
}

usuario = pd.DataFrame([dados])
usuario = usuario.reindex(columns=modelo.feature_names_in_, fill_value=0)

previsao = modelo.predict(usuario)

print("\n===== RESULTADO =====")
print("Engajamento previsto:", previsao[0])