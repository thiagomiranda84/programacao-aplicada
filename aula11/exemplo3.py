
numeros = [10,5,3,4,8,10,22,8,7]
#Realizo uma copia dos valores da lista numeros para Outra_lista
outra_lista = numeros[:]

#outra_lista = numeros -> outra_lista aponta para o mesmo local na moeria que numeros o que for alterado em um é alterado em ambos


print("Lista 1: {}".format(numeros))
print("Lista 2: {}".format(outra_lista))

outra_lista.append(1)
print("Lista 1: {}".format(numeros))
print("Lista 2: {}".format(outra_lista))

