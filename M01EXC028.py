#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

from random import choice
from time import sleep
c= 0,1,2,3,4,5 #ou radint(0,5)
b= choice(c) #ou radint(0,5)
print('-=-' * 19)
print('Vou Pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 19)
a= int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if a == b:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('ERROU! Eu pensei no número {}'.format(b))
