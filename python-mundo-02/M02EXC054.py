#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 20, 2023                                  #
#===================================================================================# 

from datetime import date as dt
atual = dt.today().year
lista = []
maior = []

for pessoa in range(1,8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoa)))
    lista.append(atual-ano)

for idade in lista:
    if idade >= 18:
        maior.append(1)
    else: maior.append(0)

print('Ao todo tivemos {} maiores de idade e {} menores de idade.'.format(maior.count(1),maior.count(0)))
