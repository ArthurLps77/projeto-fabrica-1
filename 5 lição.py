# 5. Cálculo de gorjeta
conta = float(input("Digite o valor da conta: R$ "))

if conta > 100:
    total = conta + (conta * 0.10)
    print(f"Total a pagar com 10% de gorjeta: R$ {total:.2f}")
else:
    total = conta + (conta * 0.05)
    print(f"Total a pagar com 5% de gorjeta: R$ {total:.2f}")
