#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 16, 2023                                  #
#===================================================================================# 

print('============ LOJAS EIKE ============')
gasto = float(input('Quanto você gastou?: '))
pag = int(input('''
Como deseja pagar?
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal 
[4] 3x ou mais no cartão: 20% de juros

Digito: '''))
if 1 >= pag or pag <= 4:
    if pag == 1:
        desc = gasto-(gasto/100*10)
        parc = 'Nessa forma de pagamento: {:.2f} reais sairão por {:.2f} reais'.format(gasto,desc)
    elif pag == 2:
        desc = gasto-(gasto/100*5)
        parc = 'Nessa forma de pagamento: {:.2f} reais sairão por {:.2f} reais'.format(gasto,desc)
    elif pag == 3:
        desc = gasto
        parc = 'Você pagará {:.2f} reais em 2x de {:.2f} reais cada'.format(desc,desc/2)
    else:
        parc = int(input('Quantas parcelas serão?: '))
        desc = (gasto/100 * 20)+gasto
        parc = 'Você pagará {:.2f} reais em {}x de {:.2f} reais cada'.format(desc,parc,desc/parc)
    print(parc)
else: print('Opção inválida, tente novamente.')
