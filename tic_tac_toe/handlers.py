def read_choice(menu):
    """
    This function reads an input from the keyboard
    and assure the data is part of a menu.
    :param menu: The menu from where the user has to choose an option.
    :return: The selected option of the user.
    """
    menu_keys = list(menu.keys())

    while True:
        keyboard_input = input("Select option: ")
        if keyboard_input in menu_keys:
            return keyboard_input