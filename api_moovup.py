import flask
import pandas as pd
import joblib

app = flask.Flask(__name__)

dados_modelo = joblib.load("modelo_engajamento.joblib")
modelo = dados_modelo["modelo"]
colunas = dados_modelo["colunas"]
encoder = dados_modelo["encoder"]

@app.route("/", methods=["GET"])
def inicio():
    return flask.jsonify({
        "projeto": "MoovUp",
        "mensagem": "API de previsao de engajamento funcionando!"
    })

@app.route("/predict", methods=["POST"])
def prever():
    dados = flask.request.get_json(silent=True)

    if not dados:
        return flask.jsonify({"erro": "Envie os dados em JSON."}), 400

    campos_obrigatorios = [
        "idade",
        "regiao",
        "transporte_principal",
        "frequencia_uso_semana",
        "pontos_acumulados",
        "pontos_resgatados",
        "bilhetes_resgatados",
        "acoes_realizadas",
        "pontuacao_engajamento"
    ]

    faltando = [campo for campo in campos_obrigatorios
                if campo not in dados]

    if faltando:
        return flask.jsonify({
            "erro": "Campos ausentes",
            "campos": faltando
        }), 400

    entrada = pd.DataFrame([dados])
    entrada = pd.get_dummies(
        entrada,
        columns=["regiao", "transporte_principal"]
    )
    entrada = entrada.reindex(columns=colunas, fill_value=0)

    previsao = modelo.predict(entrada)[0]
    nivel = encoder.inverse_transform([previsao])[0]

    return flask.jsonify({
        "projeto": "MoovUp",
        "nivel_engajamento_previsto": str(nivel)
    })

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
