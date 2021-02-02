"""
Brian Prost
lab_3.py
"""
import string
import time

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

us_state_data = {
    'alabama': {
        "state": "Alabama",
        "abbreviation": "AL",
        "capital": "Montgomery",
        "flower": "Camellia",
        "population": 4903185
    },
    'alaska': {
        "state": "Alaska",
        "abbreviation": "AK",
        "capital": "Juneau",
        "flower": "Forget-me-not",
        "population": 731545
    },
    'arizona': {
        "state": "Arizona",
        "abbreviation": "AZ",
        "capital": "Phoenix",
        "flower": "Saguaro Cactus Blossom",
        "population": 7278717
    },
    'arkansas': {
        "state": "Arkansas",
        "abbreviation": "AR",
        "capital": "Little Rock",
        "flower": "Apple Blossom",
        "population": 3017804
    },
    'california': {
        "state": "California",
        "abbreviation": "CA",
        "capital": "Sacramento",
        "flower": "Golden Poppy",
        "population": 39512223
    },
    'colorado': {
        "state": "Colorado",
        "abbreviation": "CO",
        "capital": "Denver",
        "flower": "Columbine",
        "population": 5758736
    },
    'connecticut': {
        "state": "Connecticut",
        "abbreviation": "CT",
        "capital": "Hartford",
        "flower": "Mountain Laurel",
        "population": 3565287
    },
    'delaware': {
        "state": "Delaware",
        "abbreviation": "DE",
        "capital": "Dover",
        "flower": "Peach Blossom",
        "population": 973764
    },
    'florida': {
        "state": "Florida",
        "abbreviation": "FL",
        "capital": "Tallahassee",
        "flower": "Orange Blossom",
        "population": 21477737
    },
    'georgia': {
        "state": "Georgia",
        "abbreviation": "GA",
        "capital": "Atlanta",
        "flower": "Cherokee Rose",
        "population": 10617423
    },
    'hawaii': {
        "state": "Hawaii",
        "abbreviation": "HI",
        "capital": "Honolulu",
        "flower": "Hibiscus",
        "population": 1415872
    },
    'idaho': {
        "state": "Idaho",
        "abbreviation": "ID",
        "capital": "Boise",
        "flower": "Syringa",
        "population": 1787065
    },
    'illinois': {
        "state": "Illinois",
        "abbreviation": "IL",
        "capital": "Springfield",
        "flower": "Native violet",
        "population": 12671821
    },
    'indiana': {
        "state": "Indiana",
        "abbreviation": "IN",
        "capital": "Indianapolis",
        "flower": "Peony",
        "population": 6732219
    },
    'iowa': {
        "state": "Iowa",
        "abbreviation": "IA",
        "capital": "Des Moines",
        "flower": "Wild Rose",
        "population": 3155070
    },
    'kansas': {
        "state": "Kansas",
        "abbreviation": "KS",
        "capital": "Topeka",
        "flower": "Native Sunflower",
        "population": 2913314
    },
    'kentucky': {
        "state": "Kentucky",
        "abbreviation": "KY",
        "capital": "Frankfort",
        "flower": "Goldenrod",
        "population": 4467673
    },
    'louisiana': {
        "state": "Louisiana",
        "abbreviation": "LA",
        "capital": "Baton Rouge",
        "flower": "Magnolia",
        "population": 4648794
    },
    'maine': {
        "state": "Maine",
        "abbreviation": "ME",
        "capital": "Augusta",
        "flower": "White Pine Cone and Tassel",
        "population": 1344212
    },
    'maryland': {
        "state": "Maryland",
        "abbreviation": "MD",
        "capital": "Annapolis",
        "flower": "Black-Eyed Susan",
        "population": 6045680
    },
    'massachusetts': {
        "state": "Massachusetts",
        "abbreviation": "MA",
        "capital": "Boston",
        "flower": "Mayflower",
        "population": 6892503
    },
    'michigan': {
        "state": "Michigan",
        "abbreviation": "MI",
        "capital": "Lansing",
        "flower": "Apple Blossom",
        "population": 9986857
    },
    'minnesota': {
        "state": "Minnesota",
        "abbreviation": "MN",
        "capital": "St. Paul",
        "flower": "Pink and White Lady’s Slipper",
        "population": 5639632
    },
    'mississippi': {
        "state": "Mississippi",
        "abbreviation": "MS",
        "capital": "Jackson",
        "flower": "Magnolia",
        "population": 2976149
    },
    'missouri': {
        "state": "Missouri",
        "abbreviation": "MO",
        "capital": "Jefferson City",
        "flower": "Hawthorn",
        "population": 6137428
    },
    'montana': {
        "state": "Montana",
        "abbreviation": "MT",
        "capital": "Helena",
        "flower": "Bitterroot",
        "population": 1068778
    },
    'nebraska': {
        "state": "Nebraska",
        "abbreviation": "NE",
        "capital": "Lincoln",
        "flower": "Goldenrod",
        "population": 1934408
    },
    'nevada': {
        "state": "Nevada",
        "abbreviation": "NV",
        "capital": "Carson City",
        "flower": "Sagebrush",
        "population": 3080156
    },
    'new hampshire': {
        "state": "New Hampshire",
        "abbreviation": "NH",
        "capital": "Concord",
        "flower": "Purple Lilac",
        "population": 1359711
    },
    'new jersey': {
        "state": "New Jersey",
        "abbreviation": "NJ",
        "capital": "Trenton",
        "flower": "Purple Violet",
        "population": 8882190
    },
    'new mexico': {
        "state": "New Mexico",
        "abbreviation": "NM",
        "capital": "Santa Fe",
        "flower": "Yucca Flower",
        "population": 2096829
    },
    'new york': {
        "state": "New York",
        "abbreviation": "NY",
        "capital": "Albany",
        "flower": "Rose",
        "population": 19453561
    },
    'north carolina': {
        "state": "North Carolina",
        "abbreviation": "NC",
        "capital": "Raleigh",
        "flower": "Dogwood",
        "population": 10488084
    },
    'north dakota': {
        "state": "North Dakota",
        "abbreviation": "ND",
        "capital": "Bismarck",
        "flower": "Wild Prairie Rose",
        "population": 762062
    },
    'ohio': {
        "state": "Ohio",
        "abbreviation": "OH",
        "capital": "Columbus",
        "flower": "Scarlet Carnation",
        "population": 11689100
    },
    'oklahoma': {
        "state": "Oklahoma",
        "abbreviation": "OK",
        "capital": "Oklahoma City",
        "flower": "Mistletoe",
        "population": 3956971
    },
    'oregon': {
        "state": "Oregon",
        "abbreviation": "OR",
        "capital": "Salem",
        "flower": "Oregon Grape",
        "population": 4217737
    },
    'pennsylvania': {
        "state": "Pennsylvania",
        "abbreviation": "PA",
        "capital": "Harrisburg",
        "flower": "Mountain Laurel",
        "population": 12801989
    },
    'rhode island': {
        "state": "Rhode Island",
        "abbreviation": "RI",
        "capital": "Providence",
        "flower": "Violet",
        "population": 1059361
    },
    'south carolina': {
        "state": "South Carolina",
        "abbreviation": "SC",
        "capital": "Columbia",
        "flower": "Yellow Jessamine",
        "population": 5148714
    },
    'south dakota': {
        "state": "South Dakota",
        "abbreviation": "SD",
        "capital": "Pierre",
        "flower": "American Pasqueflower",
        "population": 884659
    },
    'tennessee': {
        "state": "Tennessee",
        "abbreviation": "TN",
        "capital": "Nashville",
        "flower": "Iris",
        "population": 6829174
    },
    'texas': {
        "state": "Texas",
        "abbreviation": "TX",
        "capital": "Austin",
        "flower": "Bluebonnet",
        "population": 28995881
    },
    'utah': {
        "state": "Utah",
        "abbreviation": "UT",
        "capital": "Salt Lake City",
        "flower": "Sego Lily",
        "population": 3205958
    },
    'vermont': {
        "state": "Vermont",
        "abbreviation": "VT",
        "capital": "Montpelier",
        "flower": "Red Clover",
        "population": 623989
    },
    'virginia': {
        "state": "Virginia",
        "abbreviation": "VA",
        "capital": "Richmond",
        "flower": "Dogwood",
        "population": 8535519
    },
    'washington': {
        "state": "Washington",
        "abbreviation": "WA",
        "capital": "Olympia",
        "flower": "Western Rhododendron",
        "population": 7614893
    },
    'west virginia': {
        "state": "West Virginia",
        "abbreviation": "WV",
        "capital": "Charleston",
        "flower": "Big Rhododendron",
        "population": 1792147
    },
    'wisconsin': {
        "state": "Wisconsin",
        "abbreviation": "WI",
        "capital": "Madison",
        "flower": "Wood Violet",
        "population": 5822434
    },
    'wyoming': {
        "state": "Wyoming",
        "abbreviation": "WY",
        "capital": "Cheyenne",
        "flower": "Indian Paintbrush",
        "population": 578759
    },
    'washington dc': {
        "state": "Washington, D.C.",
        "abbreviation": "DC",
        "capital": "District of Columbia",
        "flower": "American Beauty Rose",
        "population": 705749
    }
}


def welcome_menu():
    """displays a welcome menu"""
    print("\nHello, and welcome to this state database thing.")
    print("Please choose an option by using a number.")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("(1) Display all U.S. States in alphabetical order, "
          "including the capital, state population, and flower.")
    print("(2) Search for a specific state, and see its capital city, "
          "population, and an image of the flower.")
    print("(3) Display a bar graph of the top 5 most populated states "
          "showing their overall population.")
    print("(4) Update the population number for a specific state.")
    print("(5) Exit the program.\n")


def operation_execution(user_choice):
    """executes the operation the user requested"""
    if user_choice == 1:  # display all states and data in alphabetical order
        display_all_states_in_alphabetical_order()
    elif user_choice == 2:  # search for state and see that info
        see_state_info()
    elif user_choice == 3:  # display a bar graph of the top 5 most populated states
        graph_most_populated_states()
    elif user_choice == 4:  # update a population number for a specific state
        update_population()
    elif user_choice == 5:  # exit program
        print("Goodbye!")
        raise SystemExit


def get_user_choice(prompt):
    """ask the user for choice and returns number of their choosing"""
    while True:
        try:
            user_choice = int(input("\t" + prompt))
            if user_choice not in range(0, 6):
                print("Please choose one of the options above.")
                continue
            return user_choice
        except ValueError:
            print("Please choose an operation by entering a number.")


def display_all_states_in_alphabetical_order():
    """displays all states"""
    # iteration for displaying data an_iterator little bit more legible
    an_iterator = 0
    for state in us_state_data:
        for data in us_state_data[state]:
            if data == 'population':
                # this will print the population with commas
                print(data.capitalize() + ': ' +
                      str(format(us_state_data[state][data], ',')))
                # time.sleep(.50)
            else:
                print(data.capitalize() + ': ' + us_state_data[state][data])
        print()
        an_iterator += 1
        if an_iterator % 2 == 0:
            time.sleep(.5)
    time.sleep(1)


def see_state_info():
    """displays info about state user requested"""
    while True:
        try:
            state_to_search = input(
                "Which state info would you like to see?\t").lower()
            if state_to_search.lower() == 'puerto rico':
                print(
                    "Unfortunately not yet...but hopefully soon! "
                    "For now, they'll just get paper towels.")
                continue
            elif state_to_search not in us_state_data.keys():
                raise KeyError
            break
        except KeyError:
            print("State not found. These are THE United States. Please try again.")
            continue
    print('Capital:\t' + us_state_data[state_to_search]['capital'])
    print('Population:\t' +
          format(us_state_data[state_to_search]['population'], ','))
    print("Here's a picture of their state flower, the "
          + string.capwords(us_state_data[state_to_search]['flower']))
    display_state_flower_image(us_state_data[state_to_search]['abbreviation'])


def display_state_flower_image(state):
    """function to display state flower image"""
    location_of_flag = 'img/flowers/' + str(state).lower() + ".jpg"
    img = mpimg.imread(location_of_flag)
    plt.imshow(img)
    plt.show()


def graph_most_populated_states():
    """graphs the five most populated states"""
    sorted_state_data_by_population = sorted(us_state_data,
                                             key=lambda x: (
                                                 us_state_data[x]['population']),
                                             reverse=True)
    states = []
    population = []
    for i in range(5):
        states.append(
            us_state_data[sorted_state_data_by_population[i]]['abbreviation'])
        population.append(
            us_state_data[sorted_state_data_by_population[i]]['population'])
    fig, ax = plt.subplots()
    width = .125
    ind = np.arange(len(population))
    ax.barh(ind, population)
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels(states, minor=False)
    plt.title('States with the Five Highest Populations')
    plt.xlabel('Population')
    plt.ylabel('State')
    plt.tick_params(axis='x', which='both', bottom=False,
                    top=False, labelbottom=False)
    for i, v in enumerate(population):
        ax.text(v + 3, i + .125, str(format(v, ',')), color='blue')
    plt.gca().invert_yaxis()
    plt.show()


def update_population():
    """updates the population for a state of user's choosing"""
    while True:
        try:
            state_to_update_population = input(
                "Which state's population would you like to change?\t").lower()
            if state_to_update_population in us_state_data.keys():
                break
            else:
                raise KeyError
        except KeyError:
            print("State not found. Please try again.")
            continue
    while True:
        try:
            new_population_size = int(
                input("What would you like the new population to be?\t"))
            break
        except ValueError:
            print("Invalid entry.")
            continue
    us_state_data[str(state_to_update_population).lower()
                  ]['population'] = new_population_size
    print(state_to_update_population.title() + "'s population is now "
          + format(new_population_size, ','))


def main():
    """main function"""
    while True:
        welcome_menu()
        user_choice = get_user_choice("What would you like to do?\t")
        operation_execution(user_choice)
        time.sleep(1)


if __name__ == '__main__':
    main()
