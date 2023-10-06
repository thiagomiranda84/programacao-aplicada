
#Iteração de Elementos de uma lista.

numeros = [10,5,7,8,9,3,2,4]
numeros.append(22)
c = 0
quantidade = len(numeros)
while(c < quantidade ):
    print("O elemento na posição {} é o {}".format(c,numeros[c]))
    c+=1

