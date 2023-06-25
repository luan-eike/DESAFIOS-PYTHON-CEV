#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 23, 2023                                  #
#===================================================================================# 

pesos = []

for pessoa in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(pessoa)))
    pesos.append(peso)

print('O maior peso informado foi {}Kg\ne o menor peso informado foi de {}Kg'.format(max(pesos),min(pesos)))
