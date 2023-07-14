from time import sleep
from random import randint as rd

jogadores = {}

for i in range(1,5):
    jogadores[f'Jogador{i}'] = rd(1,6)

for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('-='*30)
print('== RANKING DOS JOGADORES ==')

for ind, i in enumerate(sorted(jogadores, key = jogadores.get, reverse=True)):
    print(f'{ind+1}° lugar: {i} com {jogadores[i]}')
    sleep(1)