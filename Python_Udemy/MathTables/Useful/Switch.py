from Operations import Operations as op


class Switch:

    def switch(operation):
        try:
            if operation == 1:
                return op.Operations.Multiplication()
            elif operation == 2:
                return op.Operations.Division()
            elif operation == 3:
                return op.Operations.Addition()
            elif operation == 4:
                return op.Operations.Subtract()
        except AttributeError:
            print("There is no such attribute")
