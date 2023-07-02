#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

a= str(input('Digite seu nome completo: ')).strip()
b= a.split()
#c= a.rfind(' ')+1#MINHA RESOLUÇÃO
d= len(b)
print('''
Muito prazer em te conhecer!
Seu primeiro nome é {}
Seu último nome é {}
'''.format(b[0],b[len(b)-1]))#MINHA RESOLUÇÃO: '.format(b[0],a[c:1000]))'
