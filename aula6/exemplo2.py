#PASSO 1 - Criar e atribuir um valor inicial a uma Variavel de Controle
controle = 1
total = 0

#PASSO 2 - CONDIÇÃO DE REPETIÇÃO
#A REPETIÇÃO VAI ACONTECER ENQUANTO A CONDIÇÃO FOR VERDADEIRA

while controle <= 4:
    quantidade1 = int(input(f"Digite a quantidade vendida no dia {controle}: "))
    faturamento1 = quantidade1 * 2.47
    total += faturamento1
    print(f"O Faturamento do dia {controle} foi R${faturamento1:.2f}")
    #Modificar a variavel de controle para que em algum momento torne a condição falsa
    controle+=1

print(f"O Total vendido foi de R${total}")