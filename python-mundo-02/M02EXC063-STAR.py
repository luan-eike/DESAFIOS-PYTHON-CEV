#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 25, 2023                                  #
#===================================================================================# 

termos = int(input('Quantos termos de Fibonacci você deseja ver? '))
tea = termos
num = [1,0]
teste = ['1','0']
while termos != 2:
    termos -= 1
    teste.insert(0,'{}'.format(num[0]+num[1]))   
    num.insert(0,num[0]+num[1])

print('~'*50)
print(' -> '.join(teste[::-1]),end=' -> FIM\n')
print('~'*50)
