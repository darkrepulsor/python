from Useful import Menu
import os


def Multiplication():
    os.system('cls') or None
    mltTable = int(
        input("\nWich multiplication table you want to see in screen? "))
    lmtMltTable = int(
        input("\nThe multiplication table must go until... Ex: 9 x 20 "))

    # Initiating count
    i = 0

    while (i <= lmtMltTable):
        result = mltTable * i
        print(str(mltTable) + " x " + str(i) + " = " + str(result))
        i = i + 1
    decision = int(input(
        "\n\nDo you want to see another multiplication table on screen? \n\t1-Yes \n\t2-No \n\n\t"))

    if (decision == 1):
        return Menu.Menu()
    else:
        print("\nThanks for using the mulplication table program!! \nUntil next time!")
