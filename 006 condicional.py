conta = float(input("valor da conta:"))
if conta >=100:
    conta_final=conta +(conta *0.1)
    print(f"obrigado seu porra, voce gastou só r${conta_final:.2f}")
else:
    conta_final=conta + (conta_final*0.5)
    print(conta_final)