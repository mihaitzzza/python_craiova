def has_won_on_row(board_config):
    for i in range(3):
        has_won_on_current_row = True
        first_row_key = str(i + 1) + "1"
        first_row_value = board_config[first_row_key]

        if first_row_value is None:
            has_won_on_current_row = False
        else:
            for j in range(1, 3):
                current_row_key = str(i + 1) + str(j + 1)
                current_row_value = board_config[current_row_key]

                if current_row_value != first_row_value:
                    has_won_on_current_row = False
                    break

        if has_won_on_current_row:
            return True

    return False


def has_won_on_column(board_config):
    for i in range(3):
        has_won_on_current_column = True
        first_column_key = "1" + str(i + 1)
        first_column_value = board_config[first_column_key]

        if first_column_value is None:
            has_won_on_current_column = False
        else:
            for j in range(1, 3):
                current_column_key = str(j + 1) + str(i + 1)
                current_column_value = board_config[current_column_key]

                if current_column_value != first_column_value:
                    has_won_on_current_column = False
                    break

        if has_won_on_current_column:
            return True

    return False


def has_won_on_primary_diagonal(board_config):
    first_primary_diagonal_value = board_config["11"]

    if first_primary_diagonal_value is None:
        return False
    else:
        for i in range(1, 3):
            current_primary_diagonal_key = str(i + 1) + str(i + 1)
            current_primary_diagonal_value = board_config[current_primary_diagonal_key]

            if current_primary_diagonal_value != first_primary_diagonal_value:
                return False

    return True


def has_won_on_secondary_diagonal(board_config):
    first_secondary_diagonal_value = board_config["13"]

    if first_secondary_diagonal_value is None:
        return False
    else:
        for i in range(1, 3):
            current_secondary_diagonal_key = str(i + 1) + str(3 - i)
            current_secondary_diagonal_value = board_config[current_secondary_diagonal_key]

            if current_secondary_diagonal_value != first_secondary_diagonal_value:
                return False

    return True
