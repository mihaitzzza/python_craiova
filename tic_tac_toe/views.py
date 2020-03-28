def format_menu_option(option, description):
    """
    This is used for formatting an option of a menu.
    :param option: The input user has to insert to select this specific option.
    :param description: The description of this specific option.
    :return: The formatted {key: value} of a menu option.
    """
    return "{}. {}".format(option, description)

def show_menu(menu):
    """
    This is used for displaying a menu in the terminal.
    :param menu: The menu to be displayed.
    """
    for key in menu:
        print(format_menu_option(key, menu[key]))
