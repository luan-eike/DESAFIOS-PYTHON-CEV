#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

a= int(input('\nDigite um número inteiro: '))
b= (a/2)
c= '{:.1f}'.format(b)
d= '.0' in c
if d == True:
    print('\no número é PAR\n')
else:
    print('\no número é IMPAR\n')
