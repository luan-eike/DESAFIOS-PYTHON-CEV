expressao = str(input('Digite uma expressão: '))
if expressao.count('(') == expressao.count(')'):
    print('Sua expressão é valida!')
else:
    print('Sua expressão está ERRADA!')