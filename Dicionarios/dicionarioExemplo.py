usuarios = {}
print(usuarios)

usuarios = {'chaves': ['Chaves do 8', '24/12/2017', 'Recep_01'],
            'quico': ['Quico das flores', '20/12/2017', 'Raiox_03']
            }
print(usuarios)
usuarios['florinda'] = ['Dona Florinda', '24/12/2017', 'Raiox_01']
print(usuarios)

print('######## Usando get para ver o usuario ########')
# busca as informações com o get escrevendo o valor da chave do dic
print(usuarios.get('quico'))


