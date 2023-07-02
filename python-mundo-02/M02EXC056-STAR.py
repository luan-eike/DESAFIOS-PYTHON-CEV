#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 23, 2023                                  #
#===================================================================================# 

# media de idade de todos
# homem mais velho + nome do mais velho
# quantidade de mulheres + menos de 20 anos

soma = 0
idadeH = 0
nomeH = ''
mulher = []
for pessoa in range(1,5):
    print('=== {}° pessoa ==='.format(pessoa))
    nome = input('Nome: ').upper()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    soma += idade
    if pessoa == 1 and sexo == 'M':
        idadeH = idade
        nomeH = nome
    if sexo == 'M' and idade > idadeH:
        idadeH = idade
        nomeH = nome
    if sexo == 'F':
        if idade < 20:
            mulher.append(0)

media = soma / 4
print('\nA idade média do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadeH,nomeH.capitalize()))
print('Existem {} mulheres com menos de 20 anos.'.format(mulher.count(0)))
