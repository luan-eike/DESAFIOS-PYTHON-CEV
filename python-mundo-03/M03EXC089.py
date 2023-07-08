continuar = 'S'
pessoas = []
aluno = 0
while continuar not in 'NNÃONAO':
    add = [str(input('Nome: ')).capitalize()]
    add.append(float(input('Nota 1: ')))
    add.append(float(input('Nota 2: ')))
    add.append((add[1]+add[2])/2)
    pessoas.append(add)
    continuar = str(input('Deseja continuar [S/N]? ')).upper()
print('-='*13)
print(f'{"N°":<5}',f'{"Nome":<10}',f'{"Média":>5}')
print('-'*35)
for i in range(0,len(pessoas)):
    print(f'{i:<5}',f'{pessoas[i][0]:<10}',f'{pessoas[i][3]:>5}')
while aluno != 999:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    else:
        print(f'Notas de {pessoas[aluno][0]} são {pessoas[aluno][1:3]}')
