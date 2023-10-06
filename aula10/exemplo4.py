
pessoas = ["MARIA Eduarda","pedro","Lara","mariana","amanda"]
#O método sort diferencia maiusculas e minusculas (CASE SENSITIVE)
pessoas.sort(key=str.lower)

#Estou fazendo o processo de ordenação transformando todas as strings em minusculas. Para Evitar erros do CASE SENSITIVE

for pessoa in pessoas:
    print(pessoa)