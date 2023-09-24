from Operations import Multiplication as mt
from Operations import Division as dv
from Operations import Addition as add
from Operations import Subtraction as sub


def Switch(operation):
    if operation == 1:
        return mt.Multiplication()
    elif operation == 2:
        return dv.Division()
    elif operation == 3:
        return add.Addition()
    elif operation == 4:
        return sub.Subtraction()
