import json
from simple_term_menu import TerminalMenu
import random

WINE_CURSOR_STYLE = ("fg_red", "bold")
WINE_HIGHLIGHT_STYLE = ("bg_red", "fg_black")


def menu():
    wine_time_options = [
        "Learn about a random wine",
        "Lookup a specific wine"
    ]
    wine_time_menu = TerminalMenu(
        wine_time_options, menu_cursor_style=WINE_CURSOR_STYLE,
        menu_highlight_style=WINE_HIGHLIGHT_STYLE)
    wine_time_choice = wine_time_menu.show()

    if (wine_time_choice == 0):
        wine = get_random_wine()
    elif (wine_time_choice == 1):
        wine = get_specific_wine()
    
    print(f"{wine['grape']}: {wine['description']}")
    stars = get_wine_stars(wine["brian's rating"])
    print(f"Brian rates it: {stars}")

def get_random_wine():
    # TODO: move to DynamoDB
    with open('wine/wines.json') as f:
        wine_db = json.load(f)

    grape_colors_in_db = list(wine_db.keys())
    grape_color = random.choice(grape_colors_in_db)

    wines_of_grape_color_in_db = list(wine_db[grape_color].keys())
    random_wine_selection = random.choice(wines_of_grape_color_in_db)

    wine = wine_db[grape_color][random_wine_selection]
    return wine
    

def get_specific_wine():
    grape_color = get_grape_color()
    
    # TODO: move to DynamoDB
    with open('wine/wines.json') as f:
        wine_db = json.load(f)

    types_of_wine = list(wine_db[grape_color].keys())
    wine_lookup_menu = TerminalMenu(types_of_wine,
                                    menu_cursor_style=WINE_CURSOR_STYLE,
                                    menu_highlight_style=WINE_HIGHLIGHT_STYLE)
    wine_lookup_choice = wine_lookup_menu.show()
    # since that returns the index of the type of wine, convert to str by lookup
    wine = wine_db[grape_color][types_of_wine[wine_lookup_choice]]
    return wine


def get_grape_color():
    grape_colors = ["Red", "White"]
    grape_color_menu = TerminalMenu(grape_colors, title="Which category of wine?",
                                    menu_cursor_style=WINE_CURSOR_STYLE,
                                    menu_highlight_style=WINE_HIGHLIGHT_STYLE)

    grape_color_choice = grape_color_menu.show()

    if (grape_color_choice == 0):
        return 'red'
    if (grape_color_choice == 1):
        return 'white'


def get_wine_stars(wine_rating):
    # TODO: move to DynamoDB
    with open('wine/wines.json') as f:
        wine_db = json.load(f)

    if wine_rating < 0:
        return "He hasn't tried this one yet! Feel free to buy him one."

    num_stars = round(wine_rating * 5)
    star_rating = ""
    for i in range(num_stars):
        star_rating += "\u2605"
    while len(star_rating) < 5:
        star_rating += "\u2606"
    return star_rating


if __name__ == "__main__":
    # cab_rating = get_wine_stars(1)
    # print(f"Cabernet Sauvignon is always {cab_rating}")
    menu()
