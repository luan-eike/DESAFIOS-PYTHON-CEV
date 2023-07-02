#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

from datetime import date
b1=int(input('\nQual ano quer analistar? '))
p2='{:.0f}'.format(b1)
if b1 == 0:
    b1 = date.today().year
if '00' in p2:
    b2= b1/400
    b3= '{:.4f}'.format(b2)
    b4= '.0000' in b3
    if b4 == False:
        print('O ano {:.0f} NÃO é BISSEXTO'.format(b1))
    else:
        print('O ano {} É BISSEXTO'.format(b1))
else:
    b2= b1/4
    b3= '{:.4f}'.format(b2)
    b4= '.0000' in b3
    if b4 == False:
        print('O ano {:.0f} NÃO é BISSEXTO'.format(b1))
    else:
        print('O ano {} É BISSEXTO'.format(b1))
