idade = int( input("Digite a sua idade: ") )

obrigado_votar = idade >= 18 and idade < 65
#as duas comparações precisam ser Verdadeiras para a pessoa
#ser obrigada a votar

print("A pessoa é obrigada a votar? {}".format(obrigado_votar))

