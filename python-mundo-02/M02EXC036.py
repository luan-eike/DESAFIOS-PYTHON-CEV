#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: August 15, 2022                                #
#===================================================================================# 

valor = float(input('Valor do imovel: '))
meses = int(input('Parcelar em quantos anos: '))
salario = float(input('Qual seu salário: '))
a= valor/(meses*12)#valor da parcela
b= 30/100*salario#30% do salário
print('Um imóvel de {} em {} anos terá parcela de R${:.2f} por mês'.format(valor,meses,a))
if a <= b:
    print('O empréstimo será concedido.')
else:
    print('O empréstimo foi NEGADO.')
