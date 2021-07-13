'''


# criou uma array
inventario = []

resposta = 's'

# enquanto a resposta for S, ira continuar rodando o while
while resposta == 's':
    # o append insere o dado dentro do inventario que é a lista
    inventario.append(input('Esquipamento: '))
    inventario.append(float(input('Valor: ')))
    inventario.append(int(input('Número Serial: ')))
    inventario.append(input('Departamento: '))
    resposta = input('Digite \'s\' para continuar: ' .lower())

# o elemento é o nome da variável dada para o que foi adicionado no inventario
for elemento in inventario:
    print(elemento)
'''
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 's'

while resposta == 's':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Serial: ')))
    departamentos.append(input('Departamento: '))
    resposta = input('Digite \'s\' para continuar: ' .lower())

for equipamento in equipamentos:
    print('Equipamento: ', equipamentos)
for valor in valores:
    print('Valor: ', valores)
for serial in seriais:
    print('Serial: ', seriais)
for departamento in departamentos:
    print('Departamento: ', departamentos)