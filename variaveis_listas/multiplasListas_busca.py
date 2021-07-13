# Lista e multiplas
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 's'

while resposta == 's':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Número Serial: ')))
    departamentos.append(input('Departamento: '))
    resposta = input('Digite \'s\' para continuar: ' .lower())
print('------' *5)

busca = input('\nDigite o nome no equipamento que deseja buscar: ')

#vai pegar o nome do equipamento e mostrar o print do valor e serial
for indice in range(0, len (equipamentos)):
    if busca == equipamentos[indice]:
        print('Valor......:', valores[indice])
        print('Serial.....:', seriais[indice])