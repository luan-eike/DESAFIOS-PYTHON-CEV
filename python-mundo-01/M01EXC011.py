#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

a=float(input('Largura da parede: '))
b=float(input('Altura da parede: '))
c=a*b
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²\nPara pintar essa parede, você precisará de {}l de tinta'.format(a,b,c,c*1/2))
# a cada 2 metro precisa de 1 litro de tinta
