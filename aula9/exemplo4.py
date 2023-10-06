
carros = ["Fusca","Gol","Fox","Opala"]

carros.remove("Gol") #Remove um elemento a partir do seu valor

#Utilizar o operador in para verificar se um elemento está ou não presente na lista. Este operador retorna True ou False.
if "Fox" in carros:
    carros.remove("Fox")
else:
    print("A Ferrari não faz parte da lista")

print(carros)