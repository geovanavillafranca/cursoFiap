equipamentos = []
valores = []
seiais = []
departamentos = []
resposta = 's'

while resposta == 's':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seiais.append(int(input('Número Serial: ')))
    departamentos.append(input('Departamento: '))
    resposta = input('Digite \'s\' para continuar: ' .lower())
print('------' *5)
# o indice é o número que define onde está armazenado um elemento dentro de uma lista, identifica os valores da lista
# ele abre a posição 0 para armazenar o dado, quando executado novamente, abrirá a posição 1..
for indice in range(0,len(equipamentos)):

    print('\nEquipamento......: ', (indice+1))
    print('Nome.............: ', equipamentos[indice])
    print('Valor............: ', valores[indice])
    print('Serial...........: ', seiais[indice])
    print('Departamento.....: ', departamentos[indice])
    print('------' *5)