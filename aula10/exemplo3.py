
idades = []
while True:
    idade = int( input("Digite uma idade ou um valor negativo para sair: ") )
    if idade < 0:
        break
    idades.append(idade)

quantidade = len(idades) #quantidade de elementos da lista
menor = min(idades) #Retorna o menor valor de uma lista
maior = max(idades) #Retorna o maior valor de uma lista
soma = sum(idades) #Retorna a soma de todos os elementos da lista
media = soma / quantidade
idades.sort(reverse=True) #Ordeno a lista de forma crescente
#Com a configuração reverse -> Ordenamos de maneira decrescente a lista
print(f"Foram cadastradas {quantidade} idades")
print(f"A menor é idade é {menor} anos")
print(f"A maior idade é {maior} anos")
print(f"A média de Idade é {media:.2f}")
print("==========****=============****=================")
for indice,idade in enumerate(idades):
    print(indice," - ",idade)