from time import sleep
from os import system
from random import choice
import platform
import socket
import threading


moves = {"Rock":"1", 
         "Paper":"2", 
         "Scissor":"3"
}

main_menu_options = {
        "Single Player": "1",
        "LAN Play": "2",
        "Exit":"x"
}

lan_play_options = {
        "Host Game": "1",
        "Join Game": "2",
        "Exit":"x"
}

def clear_screen():
    os = platform.system()

    if os == "Windows": system("cls")
    elif os == "Darwin" or os == "Linux": system("clear")
    else: print(os)

def print_menu(options):
    clear_screen()
    if not isinstance(options, dict): return
    for option in options.keys(): print(f"{options[option]}) {option}")

def get_menu_option(options):
    if not isinstance(options, dict): return

    while True:
        user_option = input(">> ").lower()
        if user_option in options.values(): return user_option
        if user_option.isnumeric() and int(user_option) in options.values(): return user_option

def print_animation(moves):
    clear_screen()
    for move in moves.keys():
        print(move)
        sleep(1)

def get_user_move(moves):
    clear_screen()

    for move in moves.keys():
        print(f"{moves[move]}) {move}")

    while True:
        user_move = input(">> ")
        for move, move_value in zip(moves.keys(), moves.values()):
            if user_move == move_value : return move

def get_bot_move(moves):
    return choice(list(moves.keys()))

def get_winner(user_move, bot_move):
    user_move = int(moves[user_move])
    bot_move = int(moves[bot_move])

    winner = None
    if user_move == bot_move: return "Draw"
    elif (user_move - bot_move)**2 == 1: winner = user_move if user_move > bot_move else bot_move
    elif (user_move - bot_move)**2 == 4: winner = user_move if user_move < bot_move else bot_move

    for move, move_value in zip(moves.keys(), moves.values()):
        if winner == int(move_value) : return move

def print_results(user_move, bot_move, winner):
    clear_screen()
    print(f"Your Move: {user_move}")
    print(f"Bot Move: {bot_move}")
    print(f"Winner: {winner}")

def get_lan_games():
    pass

def host_game(game_name):
    print("Hosting game!")
    sleep(3)

def get_game_name():
    clear_screen()
    game_name = input("Enter game name: ")
    if game_name == input("Confirm game name: "): return game_name
    print("Game name did not match! ")
    input("Press enter to continue...")
    return


while True:
    print_menu(main_menu_options)
    main_menu_option = get_menu_option(main_menu_options)

    if main_menu_option == "x": break
    elif main_menu_option == "1":
        print_animation(moves)
        user_move = get_user_move(moves)
        bot_move = get_bot_move(moves)
        winner = get_winner(user_move, bot_move)
        print_results(user_move, bot_move, winner)
        input("Press enter to continue... ")

    elif main_menu_option == "2":
        print_menu(lan_play_options)
        lan_play_option = get_menu_option(lan_play_options)
        if lan_play_option == "1":
            game_name = get_game_name()
            if game_name == None: continue
            host_game(game_name)
        elif lan_play_option == "2":
            lan_games = get_lan_games()