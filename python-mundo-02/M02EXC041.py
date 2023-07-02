#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 16, 2023                                  #
#===================================================================================# 

from datetime import date as dt
ano = dt.today().year
nasc = int(input('digite ano de nascimento: '))
idade = ano-nasc

print('o atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('classificação: MIRIM')
elif idade <= 14:
    print('classificação: INFANTIL')
elif idade <= 19:
    print('classificação: JÚNIOR')
elif idade <= 24:
    print('classificação: SÊNIOR')
elif idade >= 25:
    print('classificação: MASTER')
