match media:
    case 0|1|2|3|4:
        print(f"Aluno(a):{nome}")
        print(f"Sua média foi {media} e você está reprovado.")
    case 5|6:
        print(f"Aluno(a):{nome}")
        print(f"Sua média foi {media} e você está de recuperação.")
    case 7|8|9|10:
        print(f"Aluno(a):{nome}")
        print(f"Sua média foi {media} e você está aprovado. Parabéns! ")
    case _:
        print("Nota inválida. Verifique as informações fornecidas.")