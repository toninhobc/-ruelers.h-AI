from flask import Flask, jsonify, request
from flask_cors import CORS
import random

RA_RANGES = {
    "Água Quente": {"min": 10, "max": 30},
    "Arniqueira": {"min": 10, "max": 30},
    "Brasília": {"min": 5, "max": 10},
    "Brazlândia": {"min": 5, "max": 55},
    "Candangolândia": {"min": 10, "max": 50},
    "Ceilândia": {"min": 10, "max": 80},
    "Cruzeiro": {"min": 5, "max": 45},
    "Fercal": {"min": 10, "max": 60},
    "Gama": {"min": 8, "max": 40},
    "Guará": {"min": 5, "max": 60},
    "Itapoã": {"min": 10, "max": 58},
    "Jardim Botânico": {"min": 5, "max": 60},
    "Lago Norte": {"min": 1, "max": 15},
    "Lago Sul": {"min": 0, "max": 10},
    "Núcleo Bandeirante": {"min": 5, "max": 45},
    "Paranoá": {"min": 12, "max": 30},
    "Parque Way": {"min": 5, "max": 40},
    "Planaltina": {"min": 15, "max": 70},
    "Recanto das Emas": {"min": 15, "max": 60},
    "Riacho Fundo": {"min": 10, "max": 70},
    "Riacho Fundo II": {"min": 10, "max": 65},
    "Samambaia": {"min": 15, "max": 80},
    "Santa Maria": {"min": 10, "max": 75},
    "São Sebastião": {"min": 10, "max": 60},
    "SCIA (Estrutural)": {"min": 10, "max": 60},
    "SIA": {"min": 15, "max": 50},
    "Sobradinho": {"min": 10, "max": 80},
    "Sobradinho II": {"min": 10, "max": 75},
    "Sudoeste/Octogonal": {"min": 5, "max": 50},
    "Taguatinga": {"min": 10, "max": 50},
    "Varjão": {"min": 12, "max": 48},
    "Vicente Pires": {"min": 5, "max": 60},
    "Sol Nascente/Pôr do Sol": {"min": 35, "max": 80},
}

app = Flask(__name__)
CORS(app)


@app.route("/risco-bairro", methods=["GET"])
# Função de teste
def obter_probabilidade():
    if request.method == "GET":
        bairro = request.args.get("bairro")

        if not bairro:
            return jsonify({"erro": "O parâmetro 'bairro' é obrigatório na URL."}), 400

        bairro_formatado = " ".join([word.capitalize() for word in bairro.split()])

        if bairro_formatado not in RA_RANGES:
            return jsonify({
                    "erro": f"Região Administrativa '{bairro_formatado}' não encontrada ou inválida."
            }
            ), 404

        ranges = RA_RANGES[bairro_formatado]
        min_val = ranges["min"]
        max_val = ranges["max"]

        random_value = random.randint(min_val, max_val) / 10000

        print(bairro)

        return jsonify({"bairro": bairro, "probabilidade": random_value}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1801)
