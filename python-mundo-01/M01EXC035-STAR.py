#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

v1=float(input('Valor 1: '))
v2=float(input('Valor 2: '))
v3=float(input('Valor 3: '))
if v1 < v3+v2 and v2 < v3+v1 and v3 < v2+v1:
    print('DA para FORMAR um triângulo.')
else:
    print('NÃO DA para FORMAR um triângulo.')
