#1 - Inicialização
valor = int( input("Digite o valor a ser sacado: ") )
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0


while valor > 0:
    if valor >= 100:
        valor -= 100
        nota100+=1
    elif valor >= 50:
        valor -= 50
        nota50+=1
    elif valor >= 20:
        valor -= 20
        nota20+=1
    elif valor >= 10:
        valor -=10
        nota10+=1
    elif valor >= 5:
        valor -= 5
        nota5+=1
    elif valor >= 2:
        valor -= 2
        nota2 +=1
    else:
        valor -=1
        nota1+=1





