#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: August 15, 2022                                #
#===================================================================================# 

import datetime as dt
nascimento = int(input('digite seu ano de nascimento: '))
ano = int(str(dt.date.today())[0:4])
idade = int(ano)-nascimento
alist = idade-18

if alist < 0:
    print('você tem {} anos, seu alistamento será em {}'.format(idade,(18-idade)+ano))
elif alist == 0:
    print('você tem {} anos, precisa se alistar esse ano'.format(idade))
else:
    print('você tem {} anos e está atrasado a {} você deveria ter se alistado em {}'.format(idade,alist,ano-idade+18))
