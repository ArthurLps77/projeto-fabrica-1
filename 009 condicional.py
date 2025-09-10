idade = int(input("porfavor informe sua idade:"))

if idade > 0:
    if idade >=18:
        print(f"voôce tem {idade} anos e é adulto")
    elif 12 <= idade <=17:
        print(f"você tem {idade} anos é adolecente")
    elif idade <=59:
        print(f"você tem {idade} anos e é adulto")
    if idade >=62:
     print(f"você tem {idade} você é um velho")