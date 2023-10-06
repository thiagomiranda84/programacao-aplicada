

numeros = [10,5,7,8,9,3,2,4]
numeros.append(22)
print(numeros)
del numeros[3] #Remove um elemento de uma determina posição na lista
numeros.pop() #Remove um elemento do final da lista
numeros.pop(1) #Ao passar uma posição esta posição será removida
quantidade = len(numeros) #LEN -> Retorna a quantidade de elementos de uma lista

print("A quantidade de elementos é {}".format(quantidade))
print(numeros)