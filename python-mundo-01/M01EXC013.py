#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

a=float(input('Qual o salário de um funcionario? '))
b= a + (a/100*15)
print('O salário do funcionário que era R${} com aumento de 15% vai para R${:.6}'.format(a,b))
