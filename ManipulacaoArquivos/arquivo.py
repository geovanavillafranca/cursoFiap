'''basedados = []
with open('iris.data', 'r') as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(','))
print(basedados)
print(basedados[0][2])
# somando os numeros, é necessario forcar a ser float primerio
print(float(basedados[0][0]) + float(basedados[0][1]))
'''

import json

dicionario = {
"FLORINDA":["DONA FLORINDA", "14/02/2017", "RECEP_01"],
  "CHAVES":["CHAVES DO 8 ", "23/02/2017", "RAIOX_02"],
  "QUICO": ["QUICO DAS FLORES", "22/02/2017", "RECEP_01"]
}

with open("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)




'''with open("bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    for chave, dados in dicionario.items():
        print(chave + " | " + str(dados))
'''