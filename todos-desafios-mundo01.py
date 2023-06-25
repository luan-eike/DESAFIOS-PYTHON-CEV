#===================================================================================#
#                            program: Python Mundo 01                               #
#                               author: Luan Eike                                   #
#                              linkedin: Luan Eike                                  #
#                              github: @luan_eike                                   #
#                                                                                   #
#                              date:  june 29, 2022                                 #
#===================================================================================# 

#==================================================== DESAFIO 001 ====================================================#
# print('Olá Mundo')

#==================================================== DESAFIO 002 ====================================================#
# resposta = input('Qual é o seu nome?')
# print(resposta)
# print('é um prazer te conhecer, {}'.format(resposta))

#==================================================== DESAFIO 003 ====================================================#
# n1=int(input('digite um number:'))
# n2=int(input('digite outro number:'))
# s=(n1+n2)
# print('o resultado é: {}'.format(s))
# print('a soma entre {} e {} é igual a {}'.format(n1,n2,s))

#==================================================== DESAFIO ### ====================================================#
# n = bool(input('digite algo'))
# print (n)

#==================================================== DESAFIO ### ====================================================#
# m = int(input('Digite um numero:'))
# m1= int(input('digite outro numero:'))
# s= (m+m1)
# print ('{} mais {} é igual a: {}'.format(m,m1,s))

#==================================================== DESAFIO ### ====================================================#
# a=(str(input('digite algo: ')))
# print('você digitou: \n {}'.format(a), end='')
# print('ola')

#==================================================== DESAFIO 005 ====================================================#
#a1=int(input('digite um numero: '))
# a2=int(a1+1)
# a3=int(a1-1)
# print('o numero é: {}, o antecessor dele é {}, e o sucessor dele é {}'.format(a1,a3,a2))
# print('o numero é: {}, o antecessor dele é {}, e o sucessor dele é {}'.format(a1,(a1-1),(a1+1)))

#==================================================== DESAFIO 006 ====================================================#
# a=int(input('digite um numero: '))
# print('o numero é: {} \no dobro de {} vale {}, \no triplo de {} vale {}, \na raiz de {} é igual a {:.3}'.format(a,a,(a*2),a,(a*3),a,(a**(1/2))))

#==================================================== DESAFIO 007 ====================================================#
# a=float(input('Primeira nota do aluno: '))
# b=float(input('Segunda nota do aluno: '))
# c=(a+b)/2
# print('A média entre {} e {} é igual a {:.2}'.format(a,b,c))

#==================================================== DESAFIO 008 ====================================================#
# a=int(input('Uma distância de metros: '))
# print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(a/1000,a/100,a/10,a*10,a*100,a*1000))

#==================================================== DESAFIO 009 ====================================================#

#============================================================================================================================= TABUADA 
# a=int(input('digite um número para ver sua tabuada: '))
# print('============\n{} x  1 = {:2}\n{} x  2 = {:2}\n{} x  3 = {:2}\n{} x  4 = {:2}\n{} x  5 = {:2}\n{} x  6 = {:2}\n{} x  7 = {:2}\n{} x  8 = {:2}\n{} x  9 = {:2}\n{} x 10 = {:2}\n============'.format(a,a,a,a*2,a,a*3,a,a*4,a,a*5,a,a*6,a,a*7,a,a*8,a,a*9,a,a*10))
#============================================================================================================================= TABUADA

#==================================================== DESAFIO 010 ====================================================#
# a=float(input('Quanto dinheiro você tem na sua carteira? '))
# print('Com R${} você pode comprar US${:.4}'.format(a,a/5.17))

#==================================================== DESAFIO 011 ====================================================#
# a=float(input('Largura da parede: '))
# b=float(input('Altura da parede: '))
# c=a*b
# print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²\nPara pintar essa parede, você precisará de {}l de tinta'.format(a,b,c,c*1/2))
#a cada 2 metro precisa de 1 litro de tinta

#==================================================== DESAFIO 012 ====================================================#
# a=float(input('Quanto custa o produto em R$? '))
# b=a/100*5
# print('O produto que custava R${}, na promoção de 5% vai custar R${}'.format(a,a-b))

#==================================================== DESAFIO 013 ====================================================#
# a=float(input('Qual o salário de um funcionario? '))
# b= a + (a/100*15)
# print('O salário do funcionário que era R${} com aumento de 15% vai para R${:.6}'.format(a,b))

#==================================================== DESAFIO 014 ====================================================#
# a=float(input('Informe a temperatura em °C: '))
# print('A temperatura de {} °C corresponde a {} °F'.format(a,a*1.8+32))

#==================================================== DESAFIO 015 ====================================================#
# a=float(input('Quantos dias o carro foi alugado? '))
# b=float(input('Quantos KM rodou? '))
# c= (a*60)+(b*0.15)
# print('O valor do aluguel é igual a R${}'.format(c))

#==================================================== DESAFIO 016 ====================================================#
# from math import floor
# a=float(input('digite um valor: '))
# print('o valor digitado foi {} e a porção inteira dele é {}'.format(a,floor(a)))

#==================================================== DESAFIO 017 ====================================================#
#================================================================= HIPOTENUSA ===================================================================================================
# a=float(input('Qual o valor do cateto oposto? '))
# b=float(input('Qual o valor do cateto adjacente? '))
# c= (a**2)+(b**2)
# print('o valor da hipotenusa é {:.2f}'.format(c**(1/2)))
#================================================================= HIPOTENUSA ===================================================================================================

#pulei o desafio 18

#==================================================== DESAFIO 019 ====================================================#
# from random import choice
# a1=input('digite o nome de um aluno: ')
# a2=input('digite o nome de outro aluno: ')
# a3=input('digite o nome de outro aluno: ')
# lista= [a1,a2,a3]
# print('O aluno escolhido foi: {}'.format(choice(lista)))

#==================================================== DESAFIO 020 ====================================================#
# from random import shuffle
# a1=input('Digite o nome de um aluno: ')
# a2=input('Digite o nome de outro aluno: ')
# a3=input('Digite o nome de outro aluno: ')
# a4=input('Digite o nome de outro aluno: ')
# lista= [a1,a2,a3,a4]
# shuffle(lista)
# print('A ordem será: ')
# print(lista)

#==================================================== DESAFIO 021 ====================================================#
#                   desafio 21 foi tocando um mp3 com biblioteca externa, eu não quis faze-lo

#==================================================== DESAFIO 022 ====================================================#
# a=str(input('Digite seu nome: ')).strip()
# UP= a.upper()
# DW= a.lower()
# sp= a.split()
# ac= ''.join(sp)
# sp1= len(ac)
# ab= len(sp[0])
# print('''Analisando seu nome...
# Seu nome em maiusculas é {}, 
# Seu nome em minusculas é {},
# Seu nome tem ao todo {} letras,
# Seu primeiro nome é {} e ele tem {} letras
# '''.format(UP,DW,sp1,sp[0],ab))

#==================================================== DESAFIO 022 ====================================================#
# a = input('digite seu nome: ')
# b = a.split()
# c = ''.join(b)
# print('''analisando seu nome...
# Maiusculo: {}
# Minusculo: {}
# Numero de letras: {}
# Primeiro nome é {}
# e tem {} letras.'''.format(a.upper(),a.lower(),c,b[0],len(b[0])))

#==================================================== DESAFIO 023 ====================================================#
# a = int(input('Informe um numero: '))
# u = a // 1 % 10
# d = a // 10 % 10
# c = a // 100 % 10
# m = a // 1000 % 10
# print('Unidade: {}'.format(u))
# print('Dezena: {}'.format(d))
# print('Centeza: {}'.format(c))
# print('Milhar: {}'.format(m))

#==================================================== DESAFIO 024 ====================================================#
# a= str(input('Em que cidade você nasceu? ').strip())
# b= a.upper()
# print('SANTO' in b)

#==================================================== DESAFIO 025 ====================================================#
# a= str(input('Qual seu nome completo? ').upper()).strip()
# print('Seu nome tem Santos?', 'SANTOS' in a)

#==================================================== DESAFIO 026 ====================================================#
# a= str(input('digite uma frase: ').lower()).strip()
# print('''
# A letra A aparece {} vezes na frase.
# A primeira letra A apareceu na posição {}.
# A última letra A apareceu na posição {}.
# '''.format(a.count('a'),a.find('a')+1,a.rfind('a')+1))

#==================================================== DESAFIO 027 ====================================================#
# a= str(input('Digite seu nome completo: ')).strip()
# b= a.split()
# #c= a.rfind(' ')+1#MINHA RESOLUÇÃO
# d= len(b)
# print('''
# Muito prazer em te conhecer!
# Seu primeiro nome é {}
# Seu último nome é {}
# '''.format(b[0],b[len(b)-1]))#MINHA RESOLUÇÃO: '.format(b[0],a[c:1000]))'

#==================================================== DESAFIO 028 ====================================================#
# from random import choice
# from time import sleep
# c= 0,1,2,3,4,5 #ou radint(0,5)
# b= choice(c) #ou radint(0,5)
# print('-=-' * 19)
# print('Vou Pensar em um número entre 0 a 5. Tente adivinhar...')
# print('-=-' * 19)
# a= int(input('Em que número eu pensei? '))
# print('PROCESSANDO...')
# sleep(2)
# if a == b:
#     print('PARABÉNS! Você conseguiu me vencer!')
# else:
#     print('ERROU! Eu pensei no número {}'.format(b))

#==================================================== DESAFIO 029 ====================================================#
# a= int(input('\nQual a velocidade do seu carro? '))
# b= (a-80)*7
# if a >= 81:
#     print('''
# MULTADO! Você excedeu o limite permitido que é 80km/h
# Você deve pagar uma multa de R$ {},00
# '''.format(b))
# else:
#     print('Dirija com segurança sempre, tenha um bom dia!')

#==================================================== DESAFIO 030 ====================================================#
# a= int(input('\nDigite um número inteiro: '))
# b= (a/2)
# c= '{:.1f}'.format(b)
# d= '.0' in c
# if d == True:
#     print('\no número é PAR\n')
# else:
#     print('\no número é IMPAR\n')


#==================================================== DESAFIO 031 ====================================================#
# a= int(input('\nQual é a distância da sua viagem? ').strip())
# print('Você está prestes a começar uma viagem de {}km.'.format(a))
# if a <= 200:
#     b= a*0.5
#     print('E o preço da sua passagem será de R${:.2f}\n'.format(b))
# else:
#     b= a*0.45
#     print('E o preço da sua passagem será de R${:.2f}\n'.format(b))

#==================================================== DESAFIO 032 ====================================================#
# from datetime import date
# ano = int(input('Qual ano quer analisar?'))
# if ano == 0:
#     ano = date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print('O ano {} é BISSEXTO'.format(ano))
# else:
#     print('O ano {} não é BISSEXTO'.format(ano))

#-=--=--=--=--=--=--=- MINHA SOLUÇÃO -=--=--=--=--=--=--=-
# from datetime import date
# b1=int(input('\nQual ano quer analistar? '))
# p2='{:.0f}'.format(b1)
# if b1 == 0:
#     b1 = date.today().year
# if '00' in p2:
#     b2= b1/400
#     b3= '{:.4f}'.format(b2)
#     b4= '.0000' in b3
#     if b4 == False:
#         print('O ano {:.0f} NÃO é BISSEXTO'.format(b1))
#     else:
#         print('O ano {} É BISSEXTO'.format(b1))
# else:
#     b2= b1/4
#     b3= '{:.4f}'.format(b2)
#     b4= '.0000' in b3
#     if b4 == False:
#         print('O ano {:.0f} NÃO é BISSEXTO'.format(b1))
#     else:
#         print('O ano {} É BISSEXTO'.format(b1))
#agora q nois descobre se tu é programador de vddkkkkkkkkkkkkj

#==================================================== DESAFIO 033 ====================================================#
# v1=int(input('\033[mPrimeiro valor: '))
# v2=int(input('\033[mSegundo valor: '))
# v3=int(input('\033[mTerceiro valor: '))
# if v1 < v2:
#     if v2 < v3:
#         maior = v3
#     else:
#         maior = v2
# else:
#     if v1 < v3:
#         maior = v3
#     else:
#         maior = v1
# if v1 > v2:
#     if v2 > v3:
#         menor = v3
#     else:
#         menor = v2
# else:
#     if v1 > v3:
#         menor = v3
#     else:
#         menor = v1
# print('\033[0;31mO MAIOR valor digitado foi \033[0;36m{:.0f}'.format(maior))
# print('\033[0;31mO MENOR valor digitado foi \033[0;36m{:.0f}'.format(menor))
#==================================================== DESAFIO 034 ====================================================#
# v1=float(input('Digite o seu salário: '))
# if v1 < 1250:
#     por = v1 * 15/100
# else:
#     por = v1 * 10/100
# sal = v1 + por
# print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(v1,sal))

#==================================================== DESAFIO 035 ====================================================#
# v1=float(input('Valor 1: '))
# v2=float(input('Valor 2: '))
# v3=float(input('Valor 3: '))
# if v1 < v3+v2 and v2 < v3+v1 and v3 < v2+v1:
#     print('DA para FORMAR um triângulo.')
# else:
#     print('NÃO DA para FORMAR um triângulo.')

#==================================================== FIM DO MUNDO 1 ====================================================#































