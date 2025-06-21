import keras.models as km
import keras
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from datetime import datetime
import json
import json


model: keras.Model
model = km.load_model('./modelos/modelo_crime.keras')

x_test = (
    "2023-02-27",
    "09:00",
    "0",
    "1",
    "20"
)

x_test = pd.DataFrame([x_test], columns=['data_ocorrencia', 'hora_ocorrencia', 'regiao_administrativa', 'sexo_vitima', "idade_vitima"])

def tempo_para_minutos(tempo):
    # Divide a string 'hh:mm' em horas e minutos
    horas, minutos = map(int, tempo.split(':'))
    
    # Converte tudo para minutos
    total_minutos = horas * 60 + minutos
    return total_minutos

x_test["hora_ocorrencia"] = x_test["hora_ocorrencia"].apply(tempo_para_minutos)

def data_para_dias(data_str):
    data = datetime.strptime(data_str, r'%Y-%m-%d')
    referencia = datetime(1970, 1, 1)
    return (data - referencia).days

x_test["data_ocorrencia"] = x_test["data_ocorrencia"].apply(data_para_dias)

scaler = MinMaxScaler()
Y = scaler.fit_transform(x_test.values.reshape(-1, 1))
Y = scaler.transform(x_test.values.reshape(-1, 1))

entrada = np.array(Y)
entrada = entrada.reshape(1, -1)

def classifica_valor(x):
    if x > 0.8: 
        return 5
    elif x > 0.6:
        return 4
    elif x > 0.4:
        return 3
    elif x > 0.2:
        return 2
    elif x >= 0.0:
        return 1

resultado = model.predict(entrada)

print(resultado)
