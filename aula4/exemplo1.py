#Python -> Tipagem Fraca e Dinâmica

# int nomevarivel -> outras linguagens

nome = "João" #String -> "" ou ''
idade = 12 #int
peso = 40.7 #Float -> Número de Ponto Flutuante -> Usa o .
#separar a casa decimal.
estuda = True #Boolean -> True ou False

#Conversão de Tipos
peso = int(peso) #int -> converte qualquer tipo para inteiro
idade = str(idade) #str -> converte qualquer tipo para string
idade = float(idade) #float -> converte qualquer tipo para float
peso = bool(peso) #bool -> converte qualquer tipo para booleano
#Caso o valor seja VAZIO ou 0 ou "" -> FALSE
#Outros valores ele apresenta TRUE

#type() -> Retornar o tipo de uma variavel ou valor
print("a Variavel nome tem o valor {} e o tipo {}"
      .format(nome,type(nome)))
print(f"O tipo de idade é {type(idade)} e o valor é {idade}")
print(type(peso))
print("O tipo da varivel estuda é %s" % type(estuda))

