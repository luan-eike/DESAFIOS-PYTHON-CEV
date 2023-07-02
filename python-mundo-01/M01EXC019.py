#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

from random import choice
a1=input('digite o nome de um aluno: ')
a2=input('digite o nome de outro aluno: ')
a3=input('digite o nome de outro aluno: ')
lista= [a1,a2,a3]
print('O aluno escolhido foi: {}'.format(choice(lista)))
