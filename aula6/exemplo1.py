lado_a = float( input("Digite o lado A: ") )
lado_b = float( input("Digite o lado B: ") )
lado_c = float( input("Digite o lado C: ") )

# lado_a < lado_b + lado_c
# lado_b < lado_a + lado_c
# lado_c < lado_a + lado_b


if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and  lado_c < lado_a + lado_b:
    print("É um Triângulo")
    if lado_a == lado_b and lado_c == lado_b:
        print("É um Triângulo Equilatero")
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
        print("É um Triângulo Isóceles")
    else:
        print("É um Triângulo Escaleno")
else:
    print("Não é um Triângulo")