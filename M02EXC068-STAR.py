#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 28, 2023                                  #
#===================================================================================# 

from random import randint 
cont = 0
computador = randint(0,9)
while True:
    jogador = int(input('Diga um valor: '))
    parimpar = str(input('Impar ou Par? [I/P]: ')).upper()
    if '.0' in str((computador+jogador)/2):
        resultado = 'PAR'
    else: resultado = 'IMPAR'
    print(f'Você jogou {jogador} e o computador {computador}. Total de {computador+jogador} deu {resultado}')
    if resultado[0] == parimpar:
        cont += 1
        print('Você VENCEU!')
    else:
        print(f'Você PERDEU! Você teve {cont} winstreak.')
        break
