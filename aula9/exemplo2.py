             #       0              1          2
ferramentas = ["Chave de Fenda","Furadeira","Martelo"]

ferramentas[2] = "Serrote" #Alterando o valor de uma posição
ferramentas[0] = "Chave Phillips"

ferramentas.append("Martelo") #Adiciona um elemento na ultima posição da lista
ferramentas.insert(1,"Parafusadeira") #adiciono um elemento em uma posição específica e realoco os elementos seguintes em novas posições.
ferramentas += ["Alicate","Parafuso"] #Operador += Adiciona uma lista ao final da lista original

print(ferramentas)

print("Elemento 0: {}".format(ferramentas[0]))
print("Elemento 1: {}".format(ferramentas[1]))
print("Elemento 2: {}".format(ferramentas[2]))
print("Elemento 3: {}".format(ferramentas[3]))
print("Elemento 4: {}".format(ferramentas[4]))