cont = 'S'
numeros = []
while cont not in 'NNÃONAO':
    numeros.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? ')).upper().strip()
print(f'Você digitou {len(numeros)} elementos')
print(f'Os valores em ordem decrescente são {sorted(numeros, reverse=True)}')
if 5 in numeros:
    res = f'apareceu {numeros.count(5)} vezes'
else:
    res = f'não apareceu'
print(f'O valor 5 {res} na lista!')
