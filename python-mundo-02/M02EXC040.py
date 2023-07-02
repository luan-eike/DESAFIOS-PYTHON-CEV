#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: August 15, 2022                                #
#===================================================================================# 

not1 = float(input('Digite a nota 1: '))
not2 = float(input('Digite a nota 2: '))
media = (not2+not1)/2
print('tirando {} e {}, a média do aluno é {}'.format(not1,not2,media))
if media >= 5 and media < 7:
    print('o aluno está de RECUPERAÇÃO')
elif media < 5:
    print('o aluno está REPROVADO')
else: print('o aluno está APROVADO')
