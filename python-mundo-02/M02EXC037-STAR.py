#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: August 15, 2022                                #
#===================================================================================# 

numero = int(input('Digite um numero inteiro: '))
print('''
Escolha a base de conversão:

1- Binário
2- Octal
3- Hexadecimal
''')
num = numero
escolha = int(input('Sua escolha: '))
lista = []
binario = 2
hexa = 16
if escolha == 3:
    while numero >= 16:
        if int(numero)%16 == 10:
            lista.append('A')
        elif int(numero)%16 == 11:
            lista.append('B')
        elif int(numero)%16 == 12:
            lista.append('C')
        elif int(numero)%16 == 13:
            lista.append('D')
        elif int(numero)%16 == 14:
            lista.append('E')
        elif int(numero)%16 == 15:
            lista.append('F')
        else: lista.append(str(int(numero)%16))
        numero = int(numero)/16
        if numero < 16:
            if int(numero) == 10:
                lista.append('A')
            elif int(numero) == 11:
                lista.append('B')
            elif int(numero) == 12:
                lista.append('C')
            elif int(numero) == 13:
                lista.append('D')
            elif int(numero) == 14:
                lista.append('E')
            elif int(numero) == 15:
                lista.append('F')
            else: lista.append(str(int(numero)))
    print('\n{} em Hexadecimal é '.format(num) + ''.join(lista[::-1]))
elif escolha == 2:
    while numero >= 8:
        lista.append(str(int(numero)%8))
        numero = int(numero)/8
    lista.append(str(int(numero)))
    print('\n{} em Octal é '.format(num) + ''.join(lista[::-1]))
elif escolha == 1:
    while numero >= 2:
        lista.append(str(int(numero)%2))
        numero = int(numero)/2
    lista.append('1')
    print('\n{} em Binário é '.format(num) + ''.join(lista[::-1]))
else: print('\nnúmero incorreto')
