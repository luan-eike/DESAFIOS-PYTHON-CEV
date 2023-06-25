#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

v1=int(input('\033[mPrimeiro valor: '))
v2=int(input('\033[mSegundo valor: '))
v3=int(input('\033[mTerceiro valor: '))
if v1 < v2:
    if v2 < v3:
        maior = v3
    else:
        maior = v2
else:
    if v1 < v3:
        maior = v3
    else:
        maior = v1
if v1 > v2:
    if v2 > v3:
        menor = v3
    else:
        menor = v2
else:
    if v1 > v3:
        menor = v3
    else:
        menor = v1
print('\033[0;31mO MAIOR valor digitado foi \033[0;36m{:.0f}'.format(maior))
print('\033[0;31mO MENOR valor digitado foi \033[0;36m{:.0f}'.format(menor))
