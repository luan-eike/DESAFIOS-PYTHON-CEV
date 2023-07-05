valores = []
par = []
impar = []
for i in range(0,7):
    num = int(input(f'Digite o {i+1}° valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
valores.append(par)
valores.append(impar)
print('-='*30)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores impares digitados foram: {sorted(valores[1])}')
