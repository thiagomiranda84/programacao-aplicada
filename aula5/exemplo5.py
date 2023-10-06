idade = int( input("Digite a sua idade: ") )
if idade >= 18 and idade <= 65: 
    print(f"A pessoa tem {idade} anos e ela é obrigada a votar")
elif idade >= 16 and idade < 18:
    print(f"A pessoa tem {idade} anos e pode votar mas não é obrigada")
elif idade > 65:
    print(f"A pessoa tem {idade} anos e pode votar mas não é obrigada")
else:
    print(f"A pessoa tem {idade} anos e NÃO PODE VOTAR")

print("FIM DA APLICAÇÃO")
