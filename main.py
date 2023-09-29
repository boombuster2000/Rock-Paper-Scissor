from time import sleep

def get_menu_option():
    options = {
        "Single Player": "1",
        "Exit":"X"
    }

    for option in options.keys(): print(f"{options[option]}) {option}")

    while True:
        user_option = input(">> ")
        if user_option in options.values(): return user_option

def print_animation():
    print("Rock")
    sleep(1)
    print("Paper")
    sleep(1)
    print("Scissor")


while True:
    menu_option = get_menu_option()

    if menu_option == "x": break
    elif menu_option == "1": 
        print_animation()
