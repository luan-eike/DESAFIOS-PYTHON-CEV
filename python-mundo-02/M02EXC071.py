#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 28, 2023                                  #
#===================================================================================# 

valor = int(input('Qual valor quer sacar? R$'))

print(f'''
Total de {int(valor/50)} cédulas de R$50
Total de {int((valor%50)/20)} cédulas de R$20
Total de {int(((valor%50)%20)/10)} cédulas de R$10
Total de {int(valor%10)} cédulas de R$1
''')
