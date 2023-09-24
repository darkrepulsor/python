import Usable


def Menu():
    operation = int(input("Wich math operation table you want to print on screen? \n\t 1 - Multiplication \n\t 2 - Division \n\t 3 - Addition \n\t 4 - Subtraction \n\t 5 - None just curious \n\n\t"))

    Usable.Switch(operation)
