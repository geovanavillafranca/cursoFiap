usuarios = {}

emails = ['xpto@xyz.com', 'xkcd@phd.com']

tupla = list(enumerate(emails))

for chave in range(0, len(tupla)):
    print('Email: ', tupla[chave][1])
    usuarios[tupla[chave]] = [input('Digite o nome: '), input('Digite o nível: ')]
print('--' * 20)
for chave, dado in usuarios.items():
    print('Usuário..:', chave[0])
    print('Email....:', chave[1])
    print('Nome.....:', dado[0])
    print('Nível....:', dado[1])
    print('--' * 20)


