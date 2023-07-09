aluno = {
    'nome': str(input('Nome: ')).capitalize(),
    'media': float(input('Média: '))
}
print('-='*30)
for key, value in aluno.items():
    print(f'- {key} é igual a {value}')
if aluno['media'] < 5:
    print('- a situação é igual a Reprovado')
elif aluno['media'] < 7:
    print('- a situação é igual a Recuperação')
else: 
    print('- a situação é igual a Aprovado')
