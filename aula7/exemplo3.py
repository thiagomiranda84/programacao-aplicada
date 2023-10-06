

#1 - Inicialização
idade = int( input("Digite uma idade ou 0 para sair") )
quantidade = 0
soma = 0

#2- Condição
while idade != 0:
    quantidade+=1
    soma += idade
    #3- modificação
    idade = int(input("Digite uma idade ou 0 para sair"))

media = soma / quantidade

print(f"A média de idade é de {media} anos e foram recebidas {quantidade} idades")

