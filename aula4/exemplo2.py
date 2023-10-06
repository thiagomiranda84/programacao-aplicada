#Entrada de dados no Python
# Função INPUT
#Ela SEMPRE RETORNA UMA STRING




num1 = input('Digite o número 1: ')
num2 = int( input('Digite o número 2: ') )
num1 = int( num1 ) #converto para inteiro

#IMPRIMO OS TIPOS RECEBIDOS NAS VARIAVEIS
#print(type(num1),type(num2))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
div_int = num1 // num2 #Divisão Inteira -> Sem casas decimais
resto = num1 % num2 #Resto da divisão
expo = num1 ** num2 #Exponenciação num1 é elevado ao num2

#10 + 5 = 15 
print(f"{num1} + {num2} = {soma}")
print("{} - {} = {}".format(num1,num2,num1-num2))
print(f"{num1} x {num2} = {mult}")
print(f"{num1} ÷ {num2} = {num1/num2}") #÷ -> alt+0247
print(f"{num1} ÷ {num2} = {div_int} com resto {resto}")
print(f"{num1} elevado {num2} = {expo}")








