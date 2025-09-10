# crie um codigo que receba informe um numero inteiro
numero=int(input("digite um numero:"))
if numero % 2 == 0:
    if numero>=10:
       print(f"o numero {numero} é par e maior que 10")
    else:
       print(f"o numero {numero} é par menor que 10")
else:
     print(f"o numero {numero} é igual a 10")