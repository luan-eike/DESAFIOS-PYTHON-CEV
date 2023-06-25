#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 20, 2023                                  #
#===================================================================================# 

num = int(input('Digite um numero: '))
lista = []
for i in range(1,num+1):
    if num % i == 0:
        lista.append(0)
    else: lista.append(1)
if lista.count(0) == 2:
    res = 'É PRIMO!'
else: res = 'NÃO É PRIMO!'
print('O numero {} foi divido {} vezes\nE por isso ele {}'.format(num,lista.count(0),res))
