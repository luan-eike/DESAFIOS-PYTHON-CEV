#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 17, 2023                                  #
#===================================================================================# 

tab = int(input('Digite um numero para ver sua tabuada: '))
for i in range(0,11):
    print('{} x {:2.0f} = '.format(tab,i), tab * i)
