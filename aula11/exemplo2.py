         #  0      1      2       3       4        5
frutas = ["Maçã","Uva","Banana","Amora","Manga","Abacaxi"]
#método index retorna o indice númerico de um valor buscado na lista
indice_uva = frutas.index("Uva")

print("O valor Uva está presente no índice {}".format(indice_uva))
print( frutas[indice_uva] )

print("=========================----========================")
#in -> operador que verifica se um valor faz parte de uma lista. Devolve True se fizer parte ou False se não fizer.
if "Jaca" in frutas:
    indice_jaca = frutas.index("Jaca")
    print("O valor Jaca está presente no índice {}".format(indice_jaca))
    print( frutas[indice_jaca] )
else:
    print("O Valor Jaca não está presente na lista")
