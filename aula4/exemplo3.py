
peso = input("Digite o seu peso em kg: ")
altura = float( input("Digite a sua altura em m: ") )

peso = float(peso)


imc = peso / (altura * altura)
#peso / altura ** 2

print(f"O imc para quem tem o peso {peso}kg e a altura {altura}m é de {imc:.2f}")
print("O imc para quem tem o peso {}kg e a altura {}m é de {:.2f}".format(peso,altura,imc))
