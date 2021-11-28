import csv
import os


def main():
    # querys
    try:
        query_sport = "hockey".lower().strip()
        query_team = "capitals".lower().strip()
        print("There was no error with the query.")
    except TypeError:
        print("There was an error with the query.")

    get_team_data(query_sport, query_team)


def get_team_data(query_sport, query_team):
    directory_path = "game_data/" + str(query_sport) + "/"

    # see if we have data
    directory_contents = [
        os.path.splitext(content)[0]
        for content in os.listdir(directory_path)
    ]

    if query_team in directory_contents:
        print("query_team in directory_contents")
        team_data_chart = directory_path + query_team + ".csv"
        with open(team_data_chart) as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                print(line)
    else:
        print(query_team in directory_contents)



def print_team_data():
    pass


if __name__ == "__main__":
    main()