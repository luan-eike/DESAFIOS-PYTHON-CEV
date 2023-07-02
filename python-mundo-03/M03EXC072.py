lista = ['zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte']
continuar = ' '

while continuar not in 'NÃONNAO':
    num = int(input('Digite um numero entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    resposta = f'Você digitou o número {lista[num]}'
    print(resposta)
    continuar = str(input('Você deseja continuar? ')).upper().strip()

print('\nPrograma encerrado, volte sempre!')