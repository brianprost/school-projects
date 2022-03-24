"""
Brian Prost
lab_5

Python script that loads one of two comma separated values (.CSV) and then performs a chosen stastical analysis on them.
"""

# imports
import pandas as pd
from millify import prettify
import matplotlib.pyplot as plt


def main():
    """main function of the program"""
    while True:
        try:
            print("^^^^ Welcome to the Python Data Analysis App ^^^^\n"
                  + "Select the file you want to analyze:\n"
                  + "(1) Population Data\n"
                  + "(2) Housing Data\n"
                  + "(3) Woah, I don't want this. Let me exit!")
            file_choice = int(input("What option would you like to do?\t"))
            if file_choice not in range(4):
                print("Please select an option 1 through 3.")
                continue
            if file_choice == 1:
                # population data
                analyze_population_data()
            elif file_choice == 2:
                analyze_housing_data()
            elif file_choice == 3:
                print("Wow. So sad. I guess I'll see you later? "
                      "No? Ok this is goodbye then.")
                raise SystemExit
        except ValueError:
            # This is stupid, I know. But it gets the point across...
            print("Beep boop, I'm a bot that only can comprehend a 1, 2, or 3. "
                  "So please use those instead of whatever you just said.")
            continue


def analyze_population_data():
    """this function loads a population data csv file, asks a user which part of the data
    they would like to analyze, and then call the print_stats function to display it."""
    print("Alright, population data.")
    population_df = pd.read_csv('csv/PopChange.csv')
    pop_column = None
    while True:
        try:
            pop_column_to_analyze = input("Select which column you would like to analyze:\n"
                                          "(a) Population April 1\n"
                                          "(b) Population July 1\n"
                                          "(c) Change in Population\n"
                                          "(d) Return to main menu\n"
                                          "    Please make a selection:\t").strip()
            if not pop_column_to_analyze or \
                    pop_column_to_analyze[0].lower() not in ('a', 'b', 'c', 'd'):
                print("Did you not read the prompt?! You are so dumb. "
                      "Please choose from the provided options.")
                continue
        except ValueError:
            print("Please choose a valid option.")
        if pop_column_to_analyze[0].lower() == 'a':
            pop_column = 'Pop Apr 1'
        elif pop_column_to_analyze[0].lower() == 'b':
            pop_column = 'Pop Jul 1'
        elif pop_column_to_analyze[0].lower() == 'c':
            pop_column = 'Change Pop'
        elif pop_column_to_analyze[0].lower() == 'd':
            break
        print_stats(population_df, pop_column)


def analyze_housing_data():
    """this function loads a housing data csv file, asks a user which part of the data
    they would like to analyze, and then call the print_stats function to display it"""
    print("Housing data it is!")
    housing_df = pd.read_csv('csv/Housing.csv')
    housing_column = None
    while True:
        try:
            housing_column_to_analyze = input("Select which column you would like to analyze:\n"
                                              "(a) Home age\n"
                                              "(b) Number of bedrooms\n"
                                              "(c) Year built\n"
                                              "(d) How many rooms\n"
                                              "(e) Cost of utilities\n"
                                              "(f) Return to main menu\n"
                                              "    Please make a selection:\t").strip()
            if not housing_column_to_analyze or \
                    housing_column_to_analyze[0].lower() not in ('a', 'b', 'c', 'd', 'e', 'f'):
                print("Did you not read the prompt?! You are so dumb. "
                      "Please choose from the provided options.")
                continue
        except TypeError:
            print("Please enter a valid input.")
        if housing_column_to_analyze[0].lower() == 'a':
            housing_column = 'AGE'
        elif housing_column_to_analyze[0].lower() == 'b':
            housing_column = 'BEDRMS'
        elif housing_column_to_analyze[0].lower() == 'c':
            housing_column = 'BUILT'
        elif housing_column_to_analyze[0].lower() == 'd':
            housing_column = 'ROOMS'
        elif housing_column_to_analyze[0].lower() == 'e':
            housing_column = 'UTILITY'
        elif housing_column_to_analyze[0].lower() == 'f':
            break
        print_stats(housing_df, housing_column)


def print_stats(data_file, column):
    """this function accepts a Pandas DataFrame and a column of user choosing
    and will create and display the data"""
    print("The statistics for this column are: ")
    print("             Count: ", prettify(data_file[column].sum().round(0)))
    print("              Mean: ", prettify(data_file[column].mean().round(2)))
    print("Standard Deviation: ", prettify(data_file[column].std().round(2)))
    print("               Min: ", prettify(data_file[column].min()))
    print("               Max: ", prettify(data_file[column].max()))
    fig, ax = plt.subplots()
    ax.hist(data_file[column])
    ax.set_title(str(column))
    fig.tight_layout()
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
