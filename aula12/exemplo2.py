

# [1,2,3,4,5] => dobro destes números => [2,4,6,8,10]


lista = [1,2,3,4,5]
dobro = []

for num in lista:
    numdobro = num * 2
    dobro.append(numdobro)

print("A lista era {} e o dobro dela é {}".format(lista,dobro))

#Compreensões de lista
dobro2 = [x*2 for x in lista]
print("A lista era {} e o dobro dela é {}".format(lista,dobro2))

metade = [x/2 for x in lista]
print("A lista era {} e o metade dela é {}".format(lista,metade))

pares = [x for x in range(20) if x % 2 == 0]
print("Pares: {}".format(pares))

#A metade de todos os números multiplos de 3 de uma lista de 0 a 100
resultado = [num/2 for num in range(101) if num % 3 == 0]
print("Resultado:{}".format(resultado))



