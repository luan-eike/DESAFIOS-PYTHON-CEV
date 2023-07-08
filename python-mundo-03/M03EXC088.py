from time import sleep
from random import randint
qtd = int(input('Quantos jogos você quer que eu sorteie? '))

def GeradorJogos():
    jogo = []
    for i in range(0,6):
        while len(jogo) != 6:
            num = randint(1,60)
            if num in jogo:
                []
            else:
                jogo.append(num)
    return jogo

print('-='*5,f'SORTEANDO {qtd} JOGOS','-='*5)
for i in range(0,qtd):
    sleep(1)
    print(f'Jogo {i+1:^3}: {sorted(GeradorJogos())}')
print('-='*5,f'{"BOA SORTE":^17}','-='*5)
