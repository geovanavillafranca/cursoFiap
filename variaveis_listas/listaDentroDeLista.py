inventario = []
resposta = 's'

while resposta == 's':
    equipamento = [input('Equipamento: '),
                  float(input('Valor: ')),
                  int(input('Número Serial: ')),
                  input('Departamento: ')]
    inventario.append(equipamento)
    resposta = input('Digite \'s\' para continuar: ').lower()

#aqui mostra a lista do inventario, os dados que foram digitados
for elemento in inventario:
    print('Nome...............:', elemento [0])
    print('Valor..............:', elemento [1])
    print('Serial.............:', elemento [2])
    print('Departamento.......:', elemento [3])
    print('------' *5)

#aqui mostra o valor e serial do equipamento que foi digitado para a busca
busca = input('\nDigite o nome do equipamento que deseja buscar: ')
for elemento in inventario:
    if busca == elemento[0]:
        print('Valor.....:', elemento [1])
        print('Serial....:', elemento [2])

depreciacao = input('\nDigite o nome do equipamento que será depreciado: ')
for elemento in inventario:
    if depreciacao == elemento[0]:
        print('Valor antigo: ', elemento [1])
        elemento [1] = elemento [1] * 0.9
        print('Novo valor: {:.2f}' .format(elemento [1]))

serial = int(input('\nDigite o serial do equipamento que será excluído:'))
for elemento in inventario:
    if elemento [2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print('Nome...............: ', elemento[0])
    print('Valor..............:', elemento[1])
    print('Serial.............:', elemento[2])
    print('Departamento.......:', elemento[3])
    print('------' *5)

valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print('O equipamento mais caro custa: {:.2f}' .format(max(valores)))
    print('O equipamento mais barato custa: {:.2f}' .format(min(valores)))
    print('O total de equipamento é de: {:.2f}' .format(sum(valores)))
