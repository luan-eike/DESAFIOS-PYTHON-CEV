#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 23, 2023                                  #
#===================================================================================# 

from random import randint as rd
number = rd(0,10)
sort = int(input('Pensei em um número de 0 a 10, tente adivinhar: '))
cont = 1
while sort != number:
    if number > sort:
        sort = int(input('Mais.. Tente novamente: '))
    else: sort = int(input('Menos.. Tente novamente: '))
    cont += 1
print('PARABÉNS, acertou com {} tentativas. O número era {}'.format(cont,number))
