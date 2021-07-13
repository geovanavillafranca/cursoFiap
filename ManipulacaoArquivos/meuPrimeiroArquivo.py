'''arquivo = open('primeiro_arquivo.txt', 'w')

arquivo.write('Meu primeiro arquivo! Ai que festa!')
arquivo.close()'''

# com esse comando, não é necessário utilizar o close() para fechar o arquivo, já fecha automaticamente
# with vai criar e as seria o nome
with open('primeiro_arquivo.txt', 'r') as arquivo:
    # arquivo.write('\nHakuna Matata!!')
    # conteudo = arquivo.read()
    for linha in arquivo.readlines():
        print(linha)




# a - append
# w - apenas cria um novo e de novo, sempre em cima do outro









