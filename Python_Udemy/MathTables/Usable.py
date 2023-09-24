import Multiplication as mt
import Division as dv


def Switch(operation):
    if operation == 1:
        return mt.Multiplication()
    elif operation == 2:
        return dv.Division()
