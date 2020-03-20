available_operations = ('+', '-', '*', '/', '=')


def format_operations_to_string():
    return ", ".join(available_operations)


def read_number():
    """
    Read a string from the keyboard.
    Assure the inserted string represents an integer number
    otherwise read until it does.
    :return: an integer number read from the keyboard
    """
    while True:
        keyboard_input = input("Operand: ")

        try:
            number = int(keyboard_input)
            break
        except ValueError:
            print("The data is not a number!")

    return number


def read_operation():
    """
    Read a string from the keyboard.
    Assure the inserted string represents an available operation
    otherwise read until it does.
    :return: a string that represents an operation
    """
    while True:
        operation = input("Operation: ")

        if operation in available_operations:
            break
        else:
            formatted_available_operations = format_operations_to_string()
            print("The operation is not available!")
            print("Please insert one of ", formatted_available_operations)

    return operation


def compute(result, number, operation):
    if operation == available_operations[0]:
        return result + number
    elif operation == available_operations[1]:
        return result - number
    elif operation == available_operations[2]:
        return result * number
    elif operation == available_operations[3]:
        operand = number
        while operand == 0:
            print("Divison by 0 is impossible. Please insert a number != 0")
            operand = read_number()
        return result / operand

    return result


def should_stop(operation):
    return operation == available_operations[-1]