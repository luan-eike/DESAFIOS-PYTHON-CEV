#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 28, 2023                                  #
#===================================================================================# 
num = 0
cont = -1
add = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    add += num
    cont += 1
print('Você digitou {} números e a soma entre eles foi de {}'.format(cont,add-999))
