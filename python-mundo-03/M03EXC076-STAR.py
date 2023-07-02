print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

tupla = ('Lapis',1.75,'Borracha',2,'Caderno',15.9,'Estojo',25,'Transferidor',4.2,'Compasso',9.99,'Mochila',120.32,'Canetas',22.3,'Livro',34.9)
for pos in range(0,len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<31}',end='')
    else:
        print(f'R$ {tupla[pos]:6.2f}')