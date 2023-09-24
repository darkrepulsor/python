# import MathTables.Useful.Switch as sw
from Useful import Switch as sw
import os


def Menu():
    os.system('cls') or None
    operation = int(input("\n\nWich math operation table you want to print on screen? \n\t 1 - Multiplication \n\t 2 - Division \n\t 3 - Addition \n\t 4 - Subtraction \n\t 5 - None just curious \n\n\t"))

    sw.Switch(operation)
