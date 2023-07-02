#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 20, 2023                                  #
#===================================================================================# 

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
inicio = int(input('primeiro termo: '))
razao = int(input('qual a razão? '))
fim = (razao*10+inicio)
for c in range(inicio,fim,razao):
    print(c,end=' -> ')
print('FIM')
