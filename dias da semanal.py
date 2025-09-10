# Crie um programa que:
# 1) Peça ao usuário que difite um número de 1 a 7 para indicar 
# os dias da semana
# 2) Use match case para exibir o nome correspondente ao número:
# 1- Domingo
# 2- Segunda-feira
# 3- Terça-feira
# 4- Quarta-feira
# 5- Quinta-feira
# 6- Sexta-feira
# 7- Sábado

dia = int(input("digite um numero de 1 a 7: "))
match dia:
    case 1:
        print("É domingo. Bom inicio de semana")
    case 2:
        print("Hoje é segunda, um dia de merda")
    case 3:
        print("hoje é terça, o dia ainda é uma bosta")
    case 4:
        print("hoje é quarta feira, esta mais ou menos o dia")
    case 5:
        print("hoje é quinta, é nornmal")
    case 6:
        print("hoje é SEXTA PLAY TV NOIS TA COMOOO")
    case 7: 
        print("hoje é sABADUMMM")