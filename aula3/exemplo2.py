#Formas de Impressão de Variaveis e Valores
nome:string = "Thiago"
altura:float = 1.8 


#Utilizando virgulas para separa valores

print(nome,'tem',altura,'m')

#Interpolação através do comando format.
#Utiliza as {} para marcar o lugar que será subtistituido
#por um determinado valor
#Podemos acrescentar modelos de formatação
#{:.2f} -> f: Float e .2 -> duas casas decimais após o .
print('{} tem {:.2f}m'.format(nome,altura))

#Interpolação através da FString
print(f'{nome} tem {altura:.2f}m')


#Concatenação
#Concatenação só funciona para Strings (textos)
#Outro tipo de dado precisa ser convertido -> str()
alturaTxt = '{:.2f}'.format(altura)
print('->'+nome+' tem '+alturaTxt+'m')













