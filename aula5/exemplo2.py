num1 = int( input("Digite um numero: ") )
num2 = int( input("Digite um numero: ") )
num3 = int( input("Digite um numero: ") )

print("O primeiro é maior que o segundo:{}".format(num1>num2))
print(f"O primeiro é maior ou igual ao terceiro:{num1>=num3}")


print(f"O segundo é menor ou igual que o terceiro:{num2<=num3}")
print(f"segundo é igual a soma do primeiro e do terceiro:{num2==num1+num3}")
print(f"O terceiro é diferente da metade do segundo:{num3 != num2/2}")
