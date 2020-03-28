from tic_tac_toe import new_game_menu, read_choice, show_menu, game_variations
from tic_tac_toe.game import get_player_names, run_game_suite


def setup_game():
    """
    This handles a whole game of tic-tac-toe between two players.
    :return: returns only if the game is stopped from the game menu.
    """
    print("\nWelcome to a new Tic-Tac-Toe game!")
    first_player, second_player = get_player_names()

    show_menu(new_game_menu)
    choice = read_choice(new_game_menu)

    if choice == list(new_game_menu.keys())[-1]:
        return

    number_of_games = game_variations[choice]
    first_player_score, second_player_score = run_game_suite(first_player, second_player, number_of_games)
    has_first_player_won = first_player_score > second_player_score
    print("\nCongrats {}, you have won the game with {}-{}".format(
        first_player if has_first_player_won else second_player,
        first_player_score if has_first_player_won else second_player_score,
        second_player_score if has_first_player_won else first_player_score
    ))