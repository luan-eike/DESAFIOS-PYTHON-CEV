#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 23, 2023                                  #
#===================================================================================# 

from time import sleep as sleep
valor1 = int(input('Primeiro Valor: '))
valor2 = int(input('Segundo Valor: '))

escolha = 0

while escolha != 5:
    escolha = int(input('''
-=-=-=-=-=-=-=-=-=-=-=-
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Escolha: '''))
    if escolha < 1 or escolha > 5:
        print('Valor incorreto, tente novamente...')
        sleep(2)
    if escolha == 1:
        print('\nA soma de {} e {} é {}'.format(valor1,valor2,valor1+valor2))
        sleep(2)
    elif escolha == 2:
        print('\nA multiplicação de {} e {} é {}'.format(valor1,valor2,valor1*valor2))
        sleep(2)
    elif escolha == 3:
        print('\nEntre {} e {} o maior valor é {}'.format(valor1,valor2,max(valor1,valor2)))
        sleep(2)
    elif escolha == 4:
        valor1 = int(input('Primeiro Valor: '))
        valor2 = int(input('Segundo Valor: '))
        print('\nValores {} e {} adicionados.'.format(valor1,valor2))
        sleep(2)
    elif escolha == 5:
        print('\nSaindo do programa...')
        sleep(2)
        print('Programa encerrado, volte sempre!')
        