brasileirao = ('Corinthians','Palmeiras','Santos','Gremio','Cruzeiro','Flamengo','Vasco da Gama', 'Chapecoense','Atlético-MG','Botafogo',
'Athletico-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória','Coritiba','Avaí','Ponte Preta','Atlético-GO')
coringudo = brasileirao.index('Corinthians')

print(f'Lista de times do Brasileirão: {brasileirao}')
print(f'\nOs 5 primeiros são: {brasileirao[0:5]}')
print(f'\nOs 4 últimos são: {brasileirao[-4:]}')
brasileirao = list(brasileirao)
brasileirao.sort()
print(f'\nTimes em orgem alfabética: {brasileirao}')
print(f'\nO CORINGÃO está na {coringudo+1}° posição')