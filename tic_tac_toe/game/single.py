from tic_tac_toe.game import select_square, display_board, has_someone_won


def run_single_game(first_player, second_player):
    """
    This is used for running a single game of tic-tac-toe and returns the winner of the game.
    :param first_player: The name of the first player.
    :param second_player: The name of the second player.
    :return: The name of the winner, or None if no one won.
    """
    print('\n{} will be the first to start.'.format(first_player))
    input("Press any key to continue...")

    board_config = {
        "11": None,
        "12": None,
        "13": None,
        "21": None,
        "22": None,
        "23": None,
        "31": None,
        "32": None,
        "33": None
    }

    step = 0
    while True:
        if step >= 9:
            print("\nThis game ended in a tie.")
            return None

        is_first_player_turn = step % 2 == 0
        active_player = first_player if is_first_player_turn else second_player
        display_board(board_config)
        selected_square = select_square(board_config, active_player)
        board_config[selected_square] = "X" if is_first_player_turn else "0"

        if has_someone_won(board_config):
            print("\nPlayer {} was one this game.".format(active_player))
            return active_player

        step += 1
