from Useful import Menu
import os


def Addition():
    os.system('cls') or None
    addTable = int(input(
        "\nWich addition table you want to see on screen? "
    ))

    lmtAddTable = int(input(
        "\nThe addition table must go until... Ex: 3 + 15\n"
    ))

    # Initiating count
    i = 0

    while (i <= lmtAddTable):
        result = addTable + i
        onScreen = str(addTable) + " + " + str(i) + " = " + str(result)
        print(onScreen)
        i = i + 1

    decision = int(input(
        "\n\nDo you want to see another addition table on screen? \n\t1-Yes \n\t2-No \n\n\t"
    ))

    if (decision == 1):
        return Menu.Menu()
    else:
        print("\nThanks for using the addition table program!! \nUntil next time!")
