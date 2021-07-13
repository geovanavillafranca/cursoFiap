from Dicionarios.funcoes import *

usuarios = {}

opcao = perguntar()

while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        cabecalho('ADICIONANDO USUÁRIO')
        inserir(usuarios)
    elif opcao == 'L':
        cabecalho('LISTANDO USUÁRIOS')
        listar()
    elif opcao == 'P':
        pesquisar()

    opcao = perguntar()
