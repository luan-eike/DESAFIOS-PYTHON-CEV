tupla = (int(input('digite um numero: ')), int(input('digite mais um numero: ')), int(input('digite outro numero: ')), int(input('digite o ultimo numero: ')))
pares = []
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}° posição')
else: print('O valor 3 não apareceu nenhuma vez')
for i in tupla:
    if i % 2 == 0:
        pares.append(str(i))
print(f'Os valores pares digitados foram {" ".join(pares)}')