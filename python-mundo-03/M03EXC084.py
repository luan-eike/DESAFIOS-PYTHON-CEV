pessoas = []
res = 'S'
peso = 0
minpeso = 0
maior = []
menor = []
while res not in 'NNÃONAO':
    dados = [str(input('Nome: ')).capitalize()]
    dados.append(int(input('Peso: ')))
    pessoas.append(dados)
    res = str(input('Deseja continuar [S/N]? ')).upper().strip()

print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
for indice, valor in enumerate(pessoas):
    if valor[1] >= peso:
        peso = valor[1]
    if minpeso == 0:
        minpeso = peso
    if valor[1] <= minpeso:
        minpeso = valor[1]
for valor in pessoas:
    if valor[1] == peso:
        maior.append(valor[0])
    if valor[1] == minpeso:
        menor.append(valor[0])
print(f'O maior peso foi de {peso}KG. Peso de {maior}')
print(f'O menor peso foi de {minpeso}KG. Peso de {menor}')
