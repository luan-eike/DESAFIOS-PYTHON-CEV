#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 28, 2023                                  #
#===================================================================================# 

#Tabuada com 6 linhas/ para sair digite um número negativo ou o número 0
num = int(input('Quer ver tabuada de qual valor? '))
while num > 0:
    for i in range(1, 11):
        print(num,'x',f'{i:02.0f}','=',num*i)
    num = int(input(30*'-','Quer ver tabuada de qual valor? '))
print('Valores encerrados, volte sempre')