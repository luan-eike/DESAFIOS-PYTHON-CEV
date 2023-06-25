#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

from random import shuffle
a1=input('Digite o nome de um aluno: ')
a2=input('Digite o nome de outro aluno: ')
a3=input('Digite o nome de outro aluno: ')
a4=input('Digite o nome de outro aluno: ')
lista= [a1,a2,a3,a4]
shuffle(lista)
print('A ordem será: ')
print(lista)
