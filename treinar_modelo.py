import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("base_moovup_500_usuarios.csv")

colunas = [
    "idade",
    "regiao",
    "transporte_principal",
    "frequencia_uso_semana",
    "pontos_acumulados",
    "pontos_resgatados",
    "bilhetes_resgatados",
    "acoes_realizadas",
    "pontuacao_engajamento",
]

X = df[colunas].copy()

X = pd.get_dummies(X, columns=["regiao", "transporte_principal"])

encoder = LabelEncoder()
y_class = encoder.fit_transform(df["nivel_engajamento"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y_class, test_size=0.2, random_state=42, stratify=y_class
)

modelo_classificacao = RandomForestClassifier(
    n_estimators=100, random_state=42
)
modelo_classificacao.fit(X_train, y_train)

previsoes = modelo_classificacao.predict(X_test)
print("Acurácia do classificador:", accuracy_score(y_test, previsoes))

joblib.dump(
    {"modelo": modelo_classificacao, "colunas": X.columns.tolist(),
     "encoder": encoder},
    "modelo_engajamento.joblib"
)

# Modelo 2: estimar pontos acumulados
X_reg = df.drop(columns=["id_usuario", "pontos_acumulados",
                         "nivel_engajamento", "pontuacao_engajamento"])
X_reg = pd.get_dummies(
    X_reg, columns=["regiao", "transporte_principal"]
)
y_reg = df["pontos_acumulados"]

Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

modelo_regressao = RandomForestRegressor(
    n_estimators=100, random_state=42
)
modelo_regressao.fit(Xr_train, yr_train)

pred_reg = modelo_regressao.predict(Xr_test)
print("Erro médio em pontos:", mean_absolute_error(yr_test, pred_reg))

joblib.dump(
    {"modelo": modelo_regressao, "colunas": X_reg.columns.tolist()},
    "modelo_pontos.joblib"
)

print("Dois modelos treinados e salvos!")
