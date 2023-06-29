#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 28, 2023                                  #
#===================================================================================# 

idade = []
mulher = 0
homem = 0
maior = 0
while True:
    print('--- CADASTRO DE PESSOA ---')
    idade.insert(0,int(input('Idade: ')))
    sexo = str(input('Sexo [M/F]: ')).upper()
    c = str(input('Quer continuar [S/N]? ')).upper()
    if sexo == 'F' and idade[0] <= 20:
        mulher += 1
    if idade[0] >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')