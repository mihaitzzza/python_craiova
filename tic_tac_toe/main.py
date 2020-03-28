from tic_tac_toe import (
    main_menu,
    show_menu,
    read_choice,
    setup_game,
)

while True:
    show_menu(main_menu)

    choice = read_choice(main_menu)
    if choice == list(main_menu.keys())[-1]:
        quit()
    else:
        setup_game()