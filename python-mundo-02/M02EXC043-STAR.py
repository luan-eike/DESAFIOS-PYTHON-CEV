#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 16, 2023                                  #
#===================================================================================# 

peso = float(input('Qual seu peso? (Kg): '))
altura = float(input('Qual sua altura? (Metro): '))

IMC = peso / (altura*altura)
if IMC > 40:
    peso = 'Obesidade Mórbida'
elif IMC >= 30:
    peso = 'Obesidade'
elif IMC >= 25:
    peso = 'Sobrepeso'
elif IMC >= 18.5:
    peso = 'Peso Ideal'
else: peso = 'Abaixo do peso'

print('Você tem o IMC de {:.1f}, e está com {}.'.format(IMC,peso))
