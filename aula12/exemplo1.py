                 # 0      1      2      3       4
classificados = ["Ana","Maria","José","Pedro","João","Eduarda","Rafaela","Lara","Alberto","Paula"]


#aprovados = classificados[0:4]
aprovados = classificados[:4]

#lista_espera = classificados[4:10]
lista_espera = classificados[4:]

print("Lista de Aprovados: {}".format(aprovados))
print("Lista de Espera: {}".format(lista_espera))

primeiro_aprovado = aprovados[0]
primeiro_lista = lista_espera[0]
print("Primeiro Aprovado: {}".format(primeiro_aprovado))
print("Primeiro Lista de Espera: {}".format(primeiro_lista))

ultimo_aprovado = aprovados[-1:]
print("Ultimo Aprovado: {}".format(ultimo_aprovado))
dois_ultimos = aprovados[-2:]
print("Dois ultimos aprovados: {}".format(dois_ultimos))
lista_espera_menos_dois = lista_espera[:-2]
print("Lista de Espera menos dois: {}".format(lista_espera_menos_dois))
