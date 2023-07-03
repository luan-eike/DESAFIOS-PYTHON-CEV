cont = 'S'
numeros = []
impar = []
par = []
while cont not in 'NNÃONAO':
    numeros.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? ')).upper().strip()
print('-='*30)
for valor in numeros:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {sorted(par)}')
print(f'A lista de impares é {sorted(impar)}')
