from random import randint as rd
sorteio = []
for i in range(0,5):
    sorteio.append(rd(0,10))
print(f'Os valores sorteados foram: {"".join(str(sorteio).replace("[","").replace("]","").replace(",",""))}')
print(f'O maior valor sorteado foi: {max(sorteio)}')
print(f'O menor valor sorteado foi: {min(sorteio)}')