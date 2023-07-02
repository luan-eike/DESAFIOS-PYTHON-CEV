resp = 'S'
lista = []
while resp not in 'NAONNÃO':
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print(f'Valor duplicado, não vou adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso.')
    resp = str(input('Deseja continuar [S/N]? ')).upper()
print('=-' * 20)
print(f'Você digitou os valores {sorted(lista)}')