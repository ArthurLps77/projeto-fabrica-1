# Tipo de triângulo
# Crie um programa que receba três lados de um triângulo
# verifique se os lados realmente podem formar um triângulo
# determine os triângulos em:
# Equilatero (todos os lados são iguais)
# Isósceles (dois lados iguais)
# Escaleno (todos os lados diferentes)

a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b:
        if b == c:
            print(f"Os lados do triangulo são {a}, {b} e {c}: triangulo equilatero")
        else:
         print(f"Os lados do triangulo são {a} {b} e {c}:triangulo isosceles.")
    else:       # não é possivel formar triangulo
     if b == c or a == c:
        print(f"Os lados do triângulo são {a}, {b} e {c}: Triângulo Isósceles.")
     else:
        print(f"Os lados do triângulo são {a}, {b} e {c}: Triângulo Escaleno.")
else:
   print ("os lados não formam um triangulo valido.")
