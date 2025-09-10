#solicitar as notas ao aluno
n1 = float(input("digite a primeira nota"))
n2 = float(input("digite a segunda nota"))
n3 = float(input("digite a terceira nota"))
#calcular media
media = (n1 + n2 + n3)/3
#chegar a condição dos alunos
#informar o resultado
if media>=7:
    print(f"o aluno tem media {media:.1f} e foi aprovado")
elif media >4:
    print(f"o aluno teve a media {media:.1f} e ficou de recuperação")
else:
    print(f"o aluno teve media{media:.1f} e esta reprovado")