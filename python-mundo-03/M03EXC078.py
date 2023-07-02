lista = []
teste = []
for i in range(0,5):
    lista.append(int(input(f'Digite um valor para posição {i}: ')))
print(f'Você digitou os valores: {lista}')
for i,v in enumerate(lista):
    if v == max(lista):
        teste.append(str(i))
print(f'O maior valor digitado foi {max(lista)} nas posições {".. ".join(teste)}',end='..')
teste = []
for i,v in enumerate(lista):
    if v == min(lista):
        teste.append(str(i))
print(f'\nO menor valor digitado foi {min(lista)} nas posições {".. ".join(teste)}',end='..')
