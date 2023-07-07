matriz = [[],[],[]]
for indice in range(0,3):
    for i in range(0,3):
        matriz[indice].append(int(input(f'Digite um valor para [{indice}, {i}]: ')))
for i in range(0,3):
    print(f'[{matriz[i][0]:^5}]',f'[{matriz[i][1]:^5}]',f'[{matriz[i][2]:^5}]')