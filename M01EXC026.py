#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

a= str(input('digite uma frase: ').lower()).strip()
print('''
A letra A aparece {} vezes na frase.
A primeira letra A apareceu na posição {}.
A última letra A apareceu na posição {}.
'''.format(a.count('a'),a.find('a')+1,a.rfind('a')+1))
