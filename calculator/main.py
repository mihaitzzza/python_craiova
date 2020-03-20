from calculator import compute, read_operation, read_number, should_stop

result = None
number = None
operation = None

while True:
    if result is None:
        result = read_number()

    operation = read_operation()

    if should_stop(operation):
        break

    number = read_number()
    result = compute(result, number, operation)
    print("Partial result: ", result)

print("Final result: ", result)