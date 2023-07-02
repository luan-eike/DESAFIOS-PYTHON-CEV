#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 16, 2023                                  #
#===================================================================================# 

#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

l1 = int(input('Primeiro segmento: '))
l2 = int(input('Segundo segmento: '))
l3 = int(input('Terceiro segmento: '))

if l1+l2 <= l3 or l1+l3 <= l2 or l2+l3 <= l1:
    print('os valores não podem formar um triangulo')
else:
    if l1 == l2 and l1 == l3:
        print('Os seguimentos podem formar um triangulo EQUILATERO')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Os segmentos podem formar um triangulo ISOSCELES')
    else: print('Os segmentos podem formar um triangulo ESCALENO')
