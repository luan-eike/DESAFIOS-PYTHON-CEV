from time import sleep
from random import randint as rd

jogadores = {}

for i in range(1,5):
    jogadores[f'Jogador{i}'] = rd(1,6)

for key, v in jogadores.items():
    print(f'O {key} tirou {v} no dado')
    # sleep(1)
print('-='*30)
print('== RANKING DOS JOGADORES ==')

# for i in range(1,5):
#     print(sorted(jogadores.values(),reverse=True))
#     print(f'{i}° lugar: {key} com {v}')

for i, v in enumerate(sorted(jogadores.values(), reverse=True)):
    for i in jogadores.values():
        if jogadores.keys() == v:
            j = jogadores.keys()
            print(f'{i+1} lugar: {j} com {v}')