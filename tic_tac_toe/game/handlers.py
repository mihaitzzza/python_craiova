import re

from tic_tac_toe.game import (
    has_won_on_row, has_won_on_column, has_won_on_primary_diagonal, has_won_on_secondary_diagonal
)

"""
Regex pattern for string with minimum 3 characters
containing any combination of lowercase letter, uppercase letter or digit.
"""
pattern = re.compile("^[a-zA-Z0-9_.-]{3,}$")
pattern_mismatch_error = "Your name should continas at least 3 characters " + \
                         "composed of any combination of lowercase, uppercase or digit."


def greet_player(player_name):
    """
    Greet player :)
    :param player_name: The name of the player to greet.
    """
    print("Hey {}, welcome to the game! Good luck!\n".format(player_name))


def print_separator_row():
    print("+---+---+---+")


def display_board(board_config):
    print('\n')
    print_separator_row()
    for i in range(3):
        current_row = "|"
        for j in range(3):
            current_key = str(i + 1) + str(j + 1)
            current_value = board_config[current_key]
            current_row += " {} |".format(current_value if current_value is not None else ' ')
        print(current_row)
        print_separator_row()


def get_player_names():
    """
    This is used for reading the name of players.
    :return: A tuple of the two player names.
    """

    first_player = None
    second_player = None

    while True:
        keyboard_input = input("Hey first player, what's your name?\n")

        if pattern.match(keyboard_input):
            greet_player(keyboard_input)

            if first_player is None:
                first_player = keyboard_input
            else:
                second_player = keyboard_input
                break
        else:
            print(pattern_mismatch_error)

    return first_player, second_player


def select_square(board_config, player):
    """
    Ask user to insert from keyboard a square where to put X or 0.
    :param board_config: The configuration of the board.
    :param player: The active player name.
    :return: The square selection of the player.
    """
    board_config_keys = list(board_config.keys())

    while True:
        keyboard_input = input("{} please select a square: ".format(player))

        if keyboard_input in board_config_keys:
            if board_config[keyboard_input] is None:
                return keyboard_input

            print("The square is not empty! Please select an empty one.")
        else:
            print("The selection is not a valid one. Please insert one of the {} values.".format(
                ", ".join(board_config_keys)))


def has_someone_won(board_config):
    """
    This helps for deciding if someone won the game or not.
    We will assume someone has won on every possible case.
    If we found at least one condition for not winning the game, we mark that case with False.
    :param board_config: The board configuration with the values
    :return: True if someone won the game or False otherwise.
    """
    if has_won_on_row(board_config):
        return True

    if has_won_on_column(board_config):
        return True

    if has_won_on_primary_diagonal(board_config):
        return True

    if has_won_on_secondary_diagonal(board_config):
        return True

    return False
