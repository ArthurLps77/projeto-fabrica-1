# 1) Entrada dos dados
salario = float(input("Informe seu salário mensal R$: "))
cargo = input("Por favor, informe seu cargo: ").strip().lower()

if cargo == "programador":
    salario_atual = salario * 1.30
    print("O novo salário do Programador é R$ {}".format(salario_atual))
elif cargo == "analista de sistemas":
    salario_atual = salario * 1.20
    print(("O novo salario do analista morto é R$ {}. ". format)(salario_atual))
elif cargo == "analista de dados":
    salario_novo = salario * 1.15
    print("O novo salário do Analista de Dados é R$ {}.".format(salario_novo))
else:
    print("Cargo não encontrado.")
