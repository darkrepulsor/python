from Useful import Menu
import os


def Subtraction():
    os.system('cls') or None
    subTable = int(input(
        "\nWich subtraction table you want to see on screen? "
    ))

    lmtSubTable = int(input(
        "\nThe subtraction table must go until... Ex: 15 - 40\n"
    ))

    # Initiating count
    i = 1

    while (i <= lmtSubTable):
        result = subTable - i
        onScreen = str(subTable) + " - " + str(i) + " = " + str(result)
        print(onScreen)
        i = i + 1

    decision = int(input(
        "\n\nDo you want to see another subtraction table on screen? \n\t1-Yes \n\t2-No \n\n\t"
    ))

    if (decision == 1):
        return Menu.Menu()
    else:
        print("\nThanks for using the subtraction table program!! \nUntil next time!")
