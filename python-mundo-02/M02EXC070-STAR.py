#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 28, 2023                                  #
#===================================================================================# 

print('-'*30,' '*5,'LOJA DO LUAN',' '*5,'-'*30)
soma = 0
caro = 0
precob = 0
barato = ''
contador = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    soma += preco
    contador += 1
    if preco > 1000:
        caro += 1
    if contador == 1:
        barato = produto
        precob = preco
    elif preco < precob:
        barato = produto
        precob = preco
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if cont == 'N':
        break
print(f'O total da compra foi de R${soma}')
print(f'Temos {caro} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custou R${precob}')