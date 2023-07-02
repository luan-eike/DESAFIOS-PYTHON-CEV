#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 17, 2023                                  #
#===================================================================================# 

c = 0 
a = 0
for i in range(0,500,3):
    if i % 3 == 0 and i % 2 != 0:
        c = c + 1
        a = a + i
print('A soma de todos os números impares ({}) que são multiplicados por três entre 1 e 500 é {}'.format(c,a))
