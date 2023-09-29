def get_menu_option():
    options = {
        "Single Player": "1",
        "Exit":"X"
    }

    for option in options.keys(): print(f"{options[option]}) {option}")

    while True:
        user_option = input(">> ")
        if user_option in options.values(): return user_option


