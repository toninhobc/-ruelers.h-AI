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
    "SCIA": {"min": 10, "max": 60},
    "SIA": {"min": 15, "max": 50},
    "Sobradinho": {"min": 10, "max": 80},
    "Sobradinho II": {"min": 10, "max": 75},
    "Sudoeste e Octogonal": {"min": 5, "max": 50},
    "Taguatinga": {"min": 10, "max": 50},
    "Varjão": {"min": 12, "max": 48},
    "Vicente Pires": {"min": 5, "max": 60},
    "Sol Nascente/Pôr do Sol": {"min": 35, "max": 80},
}

W_HORA_OCORRENCIA = {
    0: 2.0,
    1: 1.9,
    2: 1.7,
    3: 1.6,
    4: 1.4,
    5: 1.3,
    6: 1.0,
    7: 1.0,
    8: 1.0,
    9: 1.0,
    10: 1.0,
    11: 1.0,
    12: 1.0,
    13: 1.0, 
    14: 1.0, 
    15: 1.0, 
    16: 1.0,
    17: 1.0, 
    18: 1.1, 
    19: 1.2, 
    20: 1.4,
    21: 1.5, 
    22: 1.7, 
    23: 1.9
}

app = Flask(__name__)
CORS(app)


@app.route("/risco-bairro", methods=["GET"])
# Função de teste
def obter_probabilidade():
    if request.method == "GET":
        regiao_administrativa = request.args.get("regiao_administrativa")
        hora_ocorrencia = request.args.get("hora_ocorrencia")

        if not regiao_administrativa :
            return jsonify({"erro": "O parâmetro 'bregiao_administrativa' é obrigatório na URL."}), 400
        
        #if not hora_ocorrencia:
        #    hora_ocorrencia = "12:00"
#
        print(hora_ocorrencia)

        bairro_formatado = " ".join([word.capitalize() for word in regiao_administrativa .split()])

        if bairro_formatado not in RA_RANGES:
            print(f"Região Administrativa '{bairro_formatado}' não encontrada ou inválida.")
            return jsonify({
                "erro": f"Região Administrativa '{bairro_formatado}' não encontrada ou inválida."
            }
            ), 404

        ranges = RA_RANGES[bairro_formatado]
        min_val = ranges["min"]
        max_val = ranges["max"]

        risco = random.randint(min_val, max_val) / 10000
        hora_inteira = int(hora_ocorrencia.split(":")[0])
        peso_horario = W_HORA_OCORRENCIA.get(hora_inteira, 1.0)  # fallback para 1.0
        risco = risco * peso_horario

        print(regiao_administrativa, risco)

        return jsonify({"regiao_administrativa": regiao_administrativa , "risco": risco}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1801)
