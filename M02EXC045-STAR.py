#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 16, 2023                                  #
#===================================================================================# 

from random import choice
from time import sleep
e1 = [1,2,3]
pc = choice(e1)
user = int(input('''Suas opções:
1 - Pedra
2 - Papel
3 - Tesoura

Qual sua jogada? '''))
if user < 1 or user > 3:
    print('Opção invalida, tente novamente')
else:
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PÔ\n\n==================')
    
    if pc == user:
        print('EMPATE\n==================')
    elif pc == 1 and user == 3:
        print('COMPUTADOR VENCEU\n==================')
    elif pc == 2 and user == 1:
        print('COMPUTADOR VENCEU\n==================')
    elif pc == 3 and user == 2:
        print('COMPUTADOR VENCEU\n==================')
    else: print('USUÁRIO VENCEU\n==================')

    if user == 1: user = 'Pedra'
    elif user == 2: user = 'Papel'
    else: user = 'Tesoura'

    if pc == 1: pc = 'Pedra'
    elif pc == 2: pc = 'Papel'
    else: pc = 'Tesoura' 

    print('''\nUsuário jogou: {}
Computador jogou: {}\n'''.format(user,pc))
