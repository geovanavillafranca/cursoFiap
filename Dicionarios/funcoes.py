def perguntar():
    return input('O que deseja realizar? \n'
              '<I> - Para inserir um usuário \n'
              '<P> - Para pesquisar um usuário \n'
              '<E> - Para excluir um usuário \n'
              '<L> - Para listar um usuário: ').upper()

def inserir(dicionario):
    dicionario[input('Digite o login:').upper()] = [input('Digite o nome: ').upper(),
                                                     input('Digite a última data de acesso: '),
                                                     input('Qual a última estacao acessada: ').upper()]
    salvar(dicionario)


def salvar(dicionario):
    with open('bd.txt', 'a') as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ':' + str(valor) + '\n')


def pesquisar():

    nome = input('Qual o login do usuário em que deseja pesquisar? ').upper()
    with open('bd.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        for valor in conteudo:
            if nome in valor:
                print(valor, end='')

            #print(valor, end='')

        #print('CHAVES' in conteudo.values())
        #print(nome in conteudo)
        '''for valor in conteudo:
            print(valor)'''
        '''print(type(conteudo))
        print(conteudo)
        print(conteudo.get(f'{nome}'))
        print(conteudo.get(nome))'''



def excluir():
    pass


def listar():
    with open('bd.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)


def cabecalho(nome):
    print('-' * 50)
    print(nome.center(50))
    print('-' * 50)


