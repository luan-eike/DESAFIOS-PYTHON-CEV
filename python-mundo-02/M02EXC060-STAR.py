#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 25, 2023                                  #
#===================================================================================# 

num = int(input('Digite um valor: '))
lista = []
soma = num
fixo = num
while num > 1:
    soma = soma * (num-1)
    lista.append(str(num))
    num = num-1
print('Calculando {}! = {} x 1 = {}'.format(fixo,' x '.join(lista),soma))
