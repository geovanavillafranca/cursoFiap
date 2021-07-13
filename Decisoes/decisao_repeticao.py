print('--'*5 + ' NÍVEIS: ADM/ USR/ GUEST' + '--'*5)
resposta = 'sim'
while resposta == 'sim':
    nivel = input('Digite o nível de acesso: ').lower()
    if nivel == 'adm' or nivel == 'usr':
        genero = input('Digite o seu gênero: ').lower()
        if nivel == 'adm':
            if genero == 'feminino':
                print('Olá, administradora ')
            else:
                print('Olá, administrador ')
        else:
            if genero == 'feminino':
                print('Olá, usuária')
            else:
                print('Olá, usuário')
    elif nivel == 'guest':
        print('Olá, visitante')
    else:
        print('Olá, desconhecido(a)')
    resposta = input('Digite sim para continuar: ').lower()