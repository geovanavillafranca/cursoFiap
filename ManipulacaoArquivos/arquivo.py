basedados = []
with open('iris.data', 'r') as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(','))
print(basedados)
print(basedados[0][2])
# somando os numeros, é necessario forcar a ser float primerio
print(float(basedados[0][0]) + float(basedados[0][1]))
