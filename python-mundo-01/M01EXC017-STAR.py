#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

a=float(input('Qual o valor do cateto oposto? '))
b=float(input('Qual o valor do cateto adjacente? '))
c= (a**2)+(b**2)
print('o valor da hipotenusa é {:.2f}'.format(c**(1/2)))
