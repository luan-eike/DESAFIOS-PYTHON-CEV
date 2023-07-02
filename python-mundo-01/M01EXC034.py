#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

v1=float(input('Digite o seu salário: '))
if v1 < 1250:
    por = v1 * 15/100
else:
    por = v1 * 10/100
sal = v1 + por
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(v1,sal))
