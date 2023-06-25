#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

a= int(input('\nQual é a distância da sua viagem? ').strip())
print('Você está prestes a começar uma viagem de {}km.'.format(a))
if a <= 200:
    b= a*0.5
    print('E o preço da sua passagem será de R${:.2f}\n'.format(b))
else:
    b= a*0.45
    print('E o preço da sua passagem será de R${:.2f}\n'.format(b))
