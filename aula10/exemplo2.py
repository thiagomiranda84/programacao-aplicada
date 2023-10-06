
caixa_ferramentas = []
while True:
    ferramenta = input("Digite uma ferramenta ou SAIR: ")

    if ferramenta == "SAIR":
        break #Finaliza uma estrutura de repetição
    caixa_ferramentas.append(ferramenta) #adicionando um elemento na lista


print("Quantidade de Ferramentas: {}".format(len(caixa_ferramentas)))
for item in caixa_ferramentas:
    print(item)

