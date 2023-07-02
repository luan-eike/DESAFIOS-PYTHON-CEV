#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

a=int(input('Uma distância de metros: '))
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(a/1000,a/100,a/10,a*10,a*100,a*1000))
