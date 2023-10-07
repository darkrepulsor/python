import Useful
import os


class Operations:
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
            return Useful.Menu.Menu()
        else:
            print(
                "\nThanks for using the mulplication table program!! \nUntil next time!")

    def Division():
        dvsTable = int(
            input("\nWich division table you want to see in screen: "))
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
            return Useful.Menu.Menu()
        else:
            print(
                "\nThanks for using the division table program!! \nUntil next time!")

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
            return Useful.Menu.Menu()
        else:
            print(
                "\nThanks for using the addition table program!! \nUntil next time!")

    def Subtract():
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
            return Useful.Menu.Menu()
        else:
            print(
                "\nThanks for using the subtraction table program!! \nUntil next time!")
