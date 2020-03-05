def read_value(value_label):
    is_int_value = False
    while not is_int_value:
        string_value = input("Write an integer value for {}: ".format(value_label))

        try:
            value = int(string_value)
            is_int_value = True
        except:
            is_int_value = False

        if not is_int_value:
            print("Let's try again! Please focus :)")

    return value


def custom_print(label, value):
    print("{} has the value of {}.".format(label, value))