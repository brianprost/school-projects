# Brian Prost
# homework_4.py
import os
from simple_term_menu import TerminalMenu
import time
from wine import wine


def homework_4():
    """Brian's fourth homework assignment."""
    print("\n\tYou made it...", end="\r")
    time.sleep(1)
    print("\tWe're so glad you're here.", end="\r")
    time.sleep(1)
    misdirection = "\tPay no attention to that man behind the curtain"
    dots = [".  ", ".. ", "...", ".. ", ".  ",
            ".  ", " . ", "  .", " . ", ".  "]
    for i in range(18):
        print((misdirection + dots[i % len(dots)]), end="\r")
        time.sleep(0.2)
    os.system("clear"), time.sleep(0.5)

    menu_options = [
        "Learn about wine",
        "View COVID-19 data",
        "Apply a filter to a photo",
        "Get a code sent to you",
        "Leave"
    ]
    terminal_menu = TerminalMenu(menu_options, title="Now that you have focused your attention, what would you like to do?",
                                 menu_cursor_style=("fg_green", "bold"), menu_highlight_style=("bg_green", "fg_black"))
    main_choice = terminal_menu.show()

    if (main_choice == 0):
        wine.menu()
    if (main_choice == 1):
        covid.menu()
    if (main_choice == 2):
        photo.menu()
    if (main_choice == 3):
        code.menu()
    if (main_choice == 4):
        print("Get out of here!\n")

        throw_table = [
            "(╯°□°)╯︵ ┻━┻",
            "(╯°□°)╯︵       ┻━┻",
            "(╯°□°)╯︵               ┻━┻",
            "(╯°□°)╯︵                      ┻━┻"
        ]
        for i in range(len(throw_table)):
            print((throw_table[i % len(throw_table)]), end="\r")
            time.sleep(0.3)
        time.sleep(1)

        walk_to_table = [
            "(ಠ_ಠ)                          ┻━┻",
            "     (ಠ_ಠ)                     ┻━┻",
            "          (ಠ_ಠ)                ┻━┻",
            "               (ಠ_ಠ)           ┻━┻",
            "                    (ಠ_ಠ)      ┻━┻",
            "                         (ಠ_ಠ) ┻━┻",
            "                        (ಠ_ಠ)︵┻━┻ ",
            "                    (ಠ_ಠ)︵┻━┻     ",
            "                (ಠ_ಠ)︵┻━┻         ",
            "            (ಠ_ಠ)︵┻━┻             ",
            "          (ಠ_ಠ)︵┻━┻               ",
            " Goodbye! (ಠ_ಠ)︵┻━┻               "
        ]
        for i in range(len(walk_to_table)):
            print(walk_to_table[i % len(walk_to_table)], end="\r")
            time.sleep(1)
        
        print()


if __name__ == "__main__":
    homework_4()
