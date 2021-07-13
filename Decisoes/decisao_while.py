numero = int(input('Digite um número: '))
while  numero < 101:
    # o \t pula uma linha
    print('\t' + str(numero))
    # quando for digitado um valor, ira somar mais 1
    # e ira imprimir ate que chegue no número do while
    numero = numero + 1
#final, o laço terminou
print('Laço encerrado...')
