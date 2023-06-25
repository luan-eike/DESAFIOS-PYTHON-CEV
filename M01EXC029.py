#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

a= int(input('\nQual a velocidade do seu carro? '))
b= (a-80)*7
if a >= 81:
    print('''
MULTADO! Você excedeu o limite permitido que é 80km/h
Você deve pagar uma multa de R$ {},00
'''.format(b))
else:
    print('Dirija com segurança sempre, tenha um bom dia!')
