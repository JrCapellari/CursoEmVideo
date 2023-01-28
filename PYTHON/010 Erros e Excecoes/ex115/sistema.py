from lib.interface import *
from time import sleep

while True:
    resp = menu(['listar cadastro', 'cadastrar pessoa', 'sair'])
    if resp == 1 or resp == 2:
        print(f'Opção {resp} escolhida')
    elif resp == 3:
        print(f'Fechando aplicação....')
        sleep(1.3)
        print('encerrado'.upper())
        break
    else:
        print('\33[31m:::ERRO::: opção inválida\33[m')








