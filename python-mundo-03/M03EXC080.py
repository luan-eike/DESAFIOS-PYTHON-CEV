lista = []
valor = int(input('Digite um valor: '))
lista.append(valor)
print('Adicionado ao final da lista.')
for i in range(0,4):
    valor = int(input('Digite um valor: '))
    if valor >= max(lista):
        lista.append(valor)
        print('Adicionado ao final da lista.')    
    elif valor <= min(lista):
        lista.insert(0,valor)
        print('Adicionado na posição 0') 
    elif valor >= lista[1] and valor <= lista[2]:
        lista.insert(2,valor)
        print('Adicionado na posição 2')
    elif valor <= lista[1] and valor >= lista[0]:
        lista.insert(1,valor)
        print('Adicionado na posição 1') 
    elif valor >= lista[2] and valor <= lista[3]:
        lista.insert(3,valor)
        print('Adicionado na posição 3') 
print('=-' * 20)
print(f'Os valores digitados em ordem foram: {lista}')