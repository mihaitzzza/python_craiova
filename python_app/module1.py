available_operators = ('+', '-', '*', '/')


def init_collector(reference_value, operator):
    if operator == '+':
        return 0
    elif operator == '-':
        return reference_value * 2
    elif operator == '*':
        return 1

    return reference_value ** 2


def compute(values, operator):
    if operator not in available_operators:
        raise Exception("Unavailable operation!")

    collector = init_collector(values[0], operator)

    for value in values:
        if operator == '+':
            collector += value
        elif operator == '-':
            collector -= value
        elif operator == '*':
            collector *= value
        else:
            collector /= value

    return collector
