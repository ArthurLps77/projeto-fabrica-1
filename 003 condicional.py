# criar um codigo python que indica se a temperatura esta boa ou nao

#etapas
# 1) solicitar temperatura para usuario
temperatura =float(input("Digire a temperatura de hoje :D :"))
if temperatura >=28:
    print(f"a temperatura de hoje é {temperatura}C e o dia esta de muito quente°")
elif temperatura >= 20:
    print(f" a temperatura de hoje é {temperatura}°C e o dia esta agradavel")
if temperatura >=10:
    print(f"a temperatura de hoje é{temperatura}°C e o dia esta frio")
else:
    print(f" a temperatura do dia é{temperatura} e o dia esta muito molestavel")