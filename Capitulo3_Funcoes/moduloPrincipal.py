from Capitulo3_Funcoes.identificadorDeFuncoes import *

minhaLista = []
print('Preenchendo')
preencherInventario(minhaLista)
print('Exibindo')
exibirInventario(minhaLista)

print('Pesquisando')
localizarPorNome(minhaLista)
print('Alterando')
depreciarPorNome(minhaLista, 20)

print('Excluindo')
#esta dentro de um print, pois recebe um retorno
print(excluirPorSerial((minhaLista)))
exibirInventario((minhaLista))

print('Resumindo')
resumirValores(minhaLista)
