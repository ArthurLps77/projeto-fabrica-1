letra = input("digite uma letra: ")

if letra.lower() in "aeiou" :#.lower trasnforma tudo na variavel em minuscula
    print(f"vogal: {letra} ")
else:
    if letra.isupper():
        print("consoante maiscula: {letra} ")
    else:
        print("consoante maiscula: {letra}")