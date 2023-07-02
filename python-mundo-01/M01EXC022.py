#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

a = input('digite seu nome: ')
b = a.split()
print('''analisando seu nome...
Maiusculo: {}
Minusculo: {}
Numero de letras: {}
Primeiro nome é {}
e tem {} letras.'''.format(a.upper(),a.lower(),len(a.replace(' ','')),b[0].capitalize(),len(b[0])))
