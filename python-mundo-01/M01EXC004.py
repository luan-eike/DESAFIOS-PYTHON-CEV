#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

algo = input('digite algo: ')
print('O tipo primitivo desse valor é: ',type(algo))
print('Só tem espaço? ',algo.isspace())
print('É um número? ',algo.isnumeric())
print('É alfabético? ',algo.isalpha())
print('É alfanumérico? ',algo.isalnum())
print('Está em maiúsculas? ',algo.isupper())
print('Está em minúsculas? ',algo.islower())
print('Está capitalizada? ',algo.istitle())
