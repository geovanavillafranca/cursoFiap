import platform
import getpass
from datetime import datetime

# informações da máquina
print("Nome máquina:...........", platform.node())
print("Arquitetura:............", platform.architecture())
print("Sistema Operacional:....", platform.system())
print("Versão do SO:...........", platform.release())
print("Processador:............", platform.processor())
print("Versão do Python:.......", platform.python_version())


print(datetime.now())

# retorna o usuário da máquina
usuario = getpass.getuser()
# mesmo não sendo um input, será possível escrever e irá retornar a senha digitada
senha = getpass.getpass("Digite sua senha:...")

if usuario == "geova" and senha == "hello":
    print("Bem vindo Adele")
else:
    print('Você não tem acesso')

