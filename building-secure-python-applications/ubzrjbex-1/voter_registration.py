"""
Brian Prost
Lab01
This is a simple application that supports voter registration.
"""

# imports
import string
import sys

# holds user data
voter_info = {
    'first name': "",
    'last name': "",
    'age': 0,
    'us citizenship': False,
    'state': "",
    'zip code': 0
}

# reference of state names and abbreviations
us_states = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL',
             'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT',
             'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI',
             'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'ALABAMA',
             'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT',
             'DELAWARE', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA',
             'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS',
             'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA',
             'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA',
             'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND',
             'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA',
             'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING',
             }


def greeter():
    """Greets the user"""
    print("Welcome to your personal Python Voter Registration!\n")
    continue_with_registration()


def continue_with_registration():
    """This function is to make sure that the user wants to continue. It is called often"""
    while True:
        try:
            continue_yes_or_no = str(
                input("Do you want to continue?\t\t").lower().strip())
        except ValueError:
            print("I didn't get that...")
            continue
        if continue_yes_or_no.isdigit():
            print("Please answer with words or y for yes, n for no")
        if continue_yes_or_no[0] == 'n':
            print("Goodbye!")
            sys.exit("User didn't want to continue.")
        elif continue_yes_or_no[0] == 'y':
            break


def get_name(prompt):
    """Gets and returns a name"""
    while True:
        try:
            name = str(input(prompt)).strip()
        except ValueError:
            print("Please enter a valid name")
            continue
        if name != "":
            break
    return name


def get_age(prompt):
    """gets and returns the user's age"""
    while True:
        try:
            user_age = int(input(prompt))
        except ValueError:
            print("Please enter a valid age.")
            continue
        if user_age < 18:
            print("Sorry, you're too young to watch C-SPAN and as so, register to vote.")
            sys.exit(int(voter_info['age']))
        elif user_age > 120:
            print("Alright, old man...you're too old for this...")
            sys.exit(int(voter_info['age']))
        else:
            break
    return user_age


def get_citizenship_status(prompt):
    """gets and returns citizenship status"""
    while True:
        try:
            citizenship_status = str(input(prompt).lower()).strip()
        except ValueError:
            print(ValueError)
            continue
        return citizenship_status[0] == 'y'


def get_state(prompt):
    """gets the state from the user"""
    while True:
        try:
            user_state = str(input(prompt)).upper().strip()
        except ValueError:
            print("Invalid entry.")
            continue
        # searches database of state names and abbreviations for verification of state
        if user_state not in us_states:
            print(
                "State not found. Please enter a current U.S. State or its abbreviation.")
            continue
        break
    # if user entered the full state name, make sure it is in proper style
    if len(user_state) > 2:
        user_state = string.capwords(user_state)
    else:
        pass
    return user_state


def get_zip_code(prompt):
    """gets zip code"""
    while True:
        try:
            zip_code = int(input(prompt))
        except ValueError:
            continue
        # i don't know how to get this to be a comparison to 00501, the lowest zip code
        if zip_code > 99950 or zip_code < 501:
            print("Not a real US zip code! Try again")
            continue
        break
    return zip_code


def questionnaire():
    """asks each question as a function call"""

    # names
    voter_info['first name'] = get_name("What is your first name?\t\t")
    voter_info['last name'] = get_name("What is your last name?\t\t\t")
    continue_with_registration()

    # age
    voter_info['age'] = get_age("How old are you?\t\t\t")
    continue_with_registration()

    # citizenship status
    voter_info['us citizenship'] = get_citizenship_status(
        "Are you a U.S. Citizen?\t\t\t")
    continue_with_registration()

    # state
    voter_info['state'] = get_state("Which state do you live in?\t\t")
    continue_with_registration()

    # zip code
    voter_info['zip code'] = get_zip_code('What zip code do you live in?\t\t')


def read_it_back():
    """Prints out all info in same order collected"""
    print("\n***Thanks for your info. Here is what you gave us:\n")
    print("Name:\t\t", voter_info['first name'], voter_info['last name'])
    print("Age:\t\t", voter_info['age'])
    print("U.S. Citizen:\t", voter_info['us citizenship'])
    print("State:\t\t", voter_info['state'])
    print("Zip Code:\t", voter_info['zip code'])
    print("\nThanks for registering to vote. **National Anthem plays in the background**")


# main calls
greeter()
questionnaire()
read_it_back()
