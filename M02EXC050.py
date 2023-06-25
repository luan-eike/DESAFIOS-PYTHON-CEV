#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 20, 2023                                  #
#===================================================================================# 

total = 0
for i in range(0, 6):
    num = int(input('digite um valor inteiro: '))
    if num % 2 != 0:
        print('Número impar desconsiderado')
    else: 
        total = total + num
print('\nAs somas dos números pares digitados é:',total,'\n')
