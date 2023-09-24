# Simples programa de tabuada para relembrar conceitos da linguagem python!

tabuada = int(input("Qual a tabuada que deseja ver na tela: "))
lmtTabuada = int(input("Deseja a tabuada até quanto? Ex: 9 x 20 "))
i = 0

while (i <= lmtTabuada):
    result = tabuada * i
    print(str(tabuada) + " x " + str(i) + " = " + str(result))
    i = i + 1
print("\nObrgiado por usar o programa de tabuada!! \nAté mais!")
