       #  0 1 2 3  4  5 6  7 8
lista = [10,8,7,5,22,30,3,77,1]



i = 0
tamanho = len(lista)
while i < tamanho:
    print("Indice: {} - Valor {}".format(i,lista[i]))
    i+=1
print("==================------=========================")

a = 0
for item in lista:
    print("Indice:{} - Valor: {}".format(a,item))
    a+=1

print("==================------=========================")
#Enumerate é uma estrutura no python que recupera o indice e o valor de um elemento da lista a cada iteração.
for indice,valor in enumerate(lista):
    print("Indice:{} - Valor:{}".format(indice,valor))

