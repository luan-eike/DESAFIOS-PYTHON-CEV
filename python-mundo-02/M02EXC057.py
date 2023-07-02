#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 23, 2023                                  #
#===================================================================================# 

sexo = input('Informe seu sexo [M/F]: ').upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos. Por favor, informe novamente: ').upper()

print('Sexo {} registrado com sucesso'.format(sexo))
