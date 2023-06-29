#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 25, 2023                                  #
#===================================================================================# 

num = int(input('Primeiro termo: '))
razao = int(input('Qual a Razão: '))
cont = 0
while cont < 9:
    cont += 1
    if cont == 1: print(num,end='')
    print(' ->',(num+razao), end='')
    num += razao
print(' -> PAUSA')
pausa = int(input('Quantos termos você quer mostrar a mais? '))
somacont = pausa
while pausa != 0:
    cont = 1
    while cont < pausa:
        num += razao
        if cont == 1: print(num,end='')
        print(' ->',(num+razao),end='')
        cont += 1
    print(' -> PAUSA')
    num += 1
    pausa = int(input('Quantos termos você quer mostrar a mais? '))
    somacont += pausa
print('FIM DO PROGRAMA - foram realizados {} termos.'.format(somacont+10))        
