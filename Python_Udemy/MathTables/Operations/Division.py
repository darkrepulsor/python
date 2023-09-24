from Useful import Menu
import os


def Division():
    dvsTable = int(input("\nWich division table you want to see in screen: "))
    lmtDvsTable = int(
        input("\nThe division table must go until... Ex: 9 / 20 "))

    i = 1

    while (i <= lmtDvsTable):
        result = float(dvsTable / i)
        print(str(dvsTable) + " / " + str(i) + " = " + str(result))
        i = i + 1

    decision = int(input(
        "\n\nDo you want to see another division table on screen? \n\t1-Yes \n\t2-No \n\n\t"))

    if (decision == 1):
        return Menu.Menu()
    else:
        print("\nThanks for using the division table program!! \nUntil next time!")
