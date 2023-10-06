#Estrutura de Repetição com Quantidade de Repetições Determinada
c = 1
while c <= 10:
    print(c)
    c+=2

#Estrutura de Repetição com Quantidade indeterminada de repetições

crianca1 = 1.52
crianca2 = 1.45
anos = 0

while crianca1 >= crianca2:
    crianca1 += 0.005
    crianca2 += 0.01
    anos += 1

print(f"A criança 2 ultrapassou a altura da criança 1 em {anos} anos")

