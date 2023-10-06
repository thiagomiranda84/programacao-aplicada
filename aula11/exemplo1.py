

numeros = [] #Lista Vazia
pares = []
impares = []

while True:
    entrada = input("Digite um número ou Sair para finalizar o programa: ")
    if entrada.lower() == "sair":
        #string.lower() -> converte uma string para minúsculo
        break #comando break finaliza a repetiçao
    num = int(entrada) #Conversão do valor de entrada para Int
    numeros.append( num ) #append -> adiciona elementos em uma lista.

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

numeros.sort() #Ordenação de Forma Crescente
pares.sort()
impares.sort()
maior_par = max(pares) #recupera o maior elemento de uma lista
maior_impar = max(impares)
menor_par = min(pares)
menor_impar = min(impares) #recupera o menor elemento de uma lista

print("Lista de Números: {}".format(numeros))
print("Lista de Pares: {}".format(pares))
print("Lista de ìmpares: {}".format(impares))
print("O maior par é {} e o maior ímpar é {}".format(maior_par,maior_impar))
print("O menor par é {} e o menor ímpar é {}".format(menor_par,menor_impar))








