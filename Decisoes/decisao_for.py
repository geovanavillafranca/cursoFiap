tabuada = int(input('Digite um número para exibir a tabuada: '))
print('Tabuada do número ', tabuada)
# dentro do range tem o inicio o fim e o encremento,
# e vai imprimir o valor da tabuada
# (1, 11, 1) comeca do numero 1 e vai parar no 10 pois para um, menor do q 11
# numero antes de que foi colocado, e encrementa de 1 em 1
for valor in range(1, 11, 1):
    #printar  a forma e depois dar o resultado, pois o valor gera os numeros para multiplicar
    print(str(tabuada) + ' x ' + str(valor) + ' = ' + str((tabuada * valor)))

