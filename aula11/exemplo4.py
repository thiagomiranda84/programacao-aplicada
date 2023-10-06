#Fatiamento de uma lista
          # 0 1 2 3 4 5  6  7 8
numeros = [10,5,3,4,8,10,22,8,7]


lista2 = numeros[:] #lista2 recebe todos os valores de numeros
print(lista2)

lista3 = numeros[4:] #Valor Inicial (incluido) : sem valor final. Desta forma a lista será copiada do indice 4 até o final
print(lista3)

lista4 = numeros[:4] #Valor Inicial vazio : valor final (não incluido). Desta forma a lista será copiada do seu ínicio até o indice anterior ao final ou seja o 3.
print(lista4)

lista5 = numeros[2:4]#valor inicial (incluido) : valor final (não incluido). Desta forma essa copia irá iniciar no indice 2 e será finalizada no indice anterior ao 4 ou seja o 3
print(lista5)

