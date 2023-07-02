tupla = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')

for indice, palavra in enumerate(tupla):
    vogal = []
    for letra in tupla[indice]:
        if letra in 'AEIOU':
            vogal.append(letra)

    print(f'Na palavra {palavra} temos {" ".join(vogal).lower()}')