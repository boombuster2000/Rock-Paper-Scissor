from time import sleep
moves = ["Rock", "Paper", "Scissor"]

def get_menu_option():
    options = {
        "Single Player": "1",
        "Exit":"x"
    }

    for option in options.keys(): print(f"{options[option]}) {option}")

    while True:
        user_option = input(">> ").lower()
        if user_option in options.values(): return user_option

def print_animation(moves):
    for move in moves:
        print(move)
        sleep(1)

while True:
    menu_option = get_menu_option()

    if menu_option == "x": break
    elif menu_option == "1": 
        print_animation(moves)