arr = [5,3,2,4,1,2]

def subsetA(arr):
    arr1 = []
    n = len(arr)
    somaArr = 0
    somaMaior1 = 0
    
    for i in arr:
        somaArr += i #calcula a soma de todos os indices de ARR
    
    while somaMaior1 < somaArr: 
        somaMaior1 += max(arr) #aqui eu somo o maior valor da array
        somaArr -= max(arr) #aqui eu tiro da soma total da array o maior valor dela
        arr1.append(max(arr)) #depois eu adiciono a outra array o maior valor da array mãe
        arr1.sort() #organizo em ordem crescente
        arr.remove(max(arr)) #aqui eu removo da array mãe o maior valor dela
    print(arr1)
    print(somaArr)
    print(somaMaior1)
    #fiz esse teste ontem, porém tive que sair de casa e não pude terminar no e-mail luaneike.contato@gmail.com, aproveitei que ja tinha perdido a chance então refiz sozinho no meu vscode, apenas com lógica, sem pesquisar nada e sem utilizar nenhuma ferramenta tipo o chatgpt. somando as horas que usei para fazer esse exercicio acho que da um total de 2h30, se eu tenho 3h ainda restaram 30min. Resolvi fazer sozinho com meu VSCode porque sou Brasileiro e quando traduzia a pagina para ler o enunciado sem precisar ficar traduzindo na mente(que toma mais atenção), a pagina traduzia o código também então ficava muito ruim raciocinar o enunciado e codar ao mesmo tempo. Muito obrigado pela oportunidade, espero nos ver em breve.
    return(arr1)
print(subsetA(arr))