# Simple multiplication program in python

tabuada = int(input("Wich multiplication table you want to see in screen: "))
lmtTabuada = int(
    input("The multiplication table must go until... Ex: 9 x 20 "))
i = 0

while (i <= lmtTabuada):
    result = tabuada * i
    print(str(tabuada) + " x " + str(i) + " = " + str(result))
    i = i + 1
print("\nThanks for using the mulplication table program!! \nUntil next time!")
