from module1 import available_operators, compute
from module2 import read_value, custom_print

errors = []
a = read_value('a')
b = read_value('b')

values = [a, b]

custom_operator = input("Let's try a custom operation: ")
try:
    custom_result = compute(values, custom_operator)
    custom_print('custom_result', custom_result)
except Exception as e:
    errors.append(str(e))

if len(errors) == 0:
    print("There weren't any errors.")
else:
    for index, error in enumerate(errors):
        print("Error No. {}: {}".format(index + 1, error))
    print('Available operations are: ', ','.join(available_operators))

print('Python is so cool!')
