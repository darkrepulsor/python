import Menu


def Multiplication():
    mltTable = int(
        input("Wich multiplication table you want to see in screen: "))
    lmtMltTable = int(
        input("The multiplication table must go until... Ex: 9 x 20 "))

    # Initiating count
    i = 0

    while (i <= lmtMltTable):
        result = mltTable * i
        print(str(mltTable) + " x " + str(i) + " = " + str(result))
        i = i + 1
    decision = int(input(
        "Do you want to see another multiplication table on screen? 1-Yes | 2-No: "))

    if (decision == 1):
        return Menu.Menu()
    else:
        print("\nThanks for using the mulplication table program!! \nUntil next time!")
