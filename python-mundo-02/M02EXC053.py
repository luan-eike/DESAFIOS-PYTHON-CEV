#===================================================================================#
#                            program: Python Mundo 02                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date: June 20, 2023                                  #
#===================================================================================# 

frase = input('Digite uma frase: ')
frase = ''.join(frase.upper().split())

if frase[::-1] == frase:
    print('\nTemos um palíndromo!!')
else: print('\nNão é um palíndromo')
print(frase+' - '+frase[::-1])
