matriz = [[],[],[]]
for indice in range(0,3):
    for i in range(0,3):
        matriz[indice].append(int(input(f'Digite um valor para [{indice}, {i}]: ')))
for indice in range(0,3):
    for i in range(0,3):
        print(matriz[indice][i])