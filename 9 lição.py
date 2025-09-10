# 9. Desconto em compras por valor mínimo
valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra > 150:
    valor_final = valor_compra - 20
    print(f"Desconto aplicado! Valor final: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. Valor final: R$ {valor_compra:.2f}")