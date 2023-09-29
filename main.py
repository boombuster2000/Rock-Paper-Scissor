from time import sleep
from os import system
from random import choice

moves = {"Rock":"1", 
         "Paper":"2", 
         "Scissor":"3"}

def get_menu_option():
    system("cls")

    options = {
        "Single Player": "1",
        "Exit":"x"
    }

    for option in options.keys(): print(f"{options[option]}) {option}")

    while True:
        user_option = input(">> ").lower()
        if user_option in options.values(): return user_option

def print_animation(moves):
    system("cls")
    for move in moves.keys():
        print(move)
        sleep(1)

def get_user_move(moves):
    system("cls")

    for move in moves.keys():
        print(f"{moves[move]}) {move}")

    while True:
        user_move = input(">> ")
        if user_move in moves.values(): return

def get_bot_move(moves):
    return choice(list(moves.keys()))

while True:
    menu_option = get_menu_option()

    if menu_option == "x": break
    elif menu_option == "1": 
        print_animation(moves)
        user_move = get_user_move(moves)
        bot_move = get_bot_move(moves)
        print(bot_move)