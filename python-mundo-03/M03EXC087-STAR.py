matriz = [[],[],[]]

def SomarPar(matriz):
    soma = 0
    for i in range(0,3):
        for indice in matriz[i]:
            if indice % 2 == 0:
                soma += indice
    return soma

for i in range(0,3):
    for indice in range(0,3):
        matriz[indice].append(int(input(f'Digite um valor para [{i}, {indice}]:')))

print('-=' * 30)
for i in range(0,3):
    print(f'[{matriz[i][0]:^5}]',f'[{matriz[i][1]:^5}]',f'[{matriz[i][2]:^5}]')
print('-=' * 30)
print(f'A soma dos valores pares é: {SomarPar(matriz)}')
print(f'A soma dos valores da terceira coluna é {matriz[2][0]+matriz[2][1]+matriz[2][2]}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')