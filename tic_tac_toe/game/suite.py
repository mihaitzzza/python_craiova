from random import choice
from tic_tac_toe.game import run_single_game


def run_game_suite(first_player, second_player, number_of_games):
    """
    This is used for running a game in the 2 out of 3 or 3 out of 5 format.
    :param first_player: The name of the first player
    :param second_player: The name of the second player
    :param number_of_games: The maximum number of the games.
    """
    current_game = 0
    minimum_games_to_won = number_of_games // 2 + 1
    first_player_score = 0
    second_player_score = 0

    print("\n{} vs {} in a {} out of {}".format(first_player, second_player, minimum_games_to_won, number_of_games))
    print("FIGHT :)")

    while True:
        player_with_X = first_player
        player_with_0 = second_player

        if current_game < number_of_games:
            if current_game % 2 == 1:
                player_with_X = second_player
                player_with_0 = first_player
        else:
            random_choice = choice([1, 2])
            if random_choice == 2:
                player_with_X = second_player
                player_with_0 = first_player

        winner = run_single_game(player_with_X, player_with_0)

        if winner == first_player:
            first_player_score += 1
        elif winner == second_player:
            second_player_score += 1

        # Display current score
        print("{} {}-{} {}".format(first_player, first_player_score, second_player_score, second_player))
        input("Press any key to continue...")

        if first_player_score == minimum_games_to_won or second_player_score == minimum_games_to_won:
            return first_player_score, second_player_score

        current_game += 1
