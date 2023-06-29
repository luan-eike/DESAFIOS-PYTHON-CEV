#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 28, 2023                                  #
#===================================================================================# 

num = cont = soma = maior = menor = 0
string = ''

while string != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if num >= maior:
        maior = num
    elif num <= num:
        menor = num
    string = str(input('Quer continuar? [N/S] ')).upper()
media = soma/cont
print('Você digitou {} números e a média é de {}'.format(cont,media))
print('O maior valor foi de {} e o menor foi {}'.format(maior,menor))
