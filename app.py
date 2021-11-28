import json
import os


def main():
    # querys
    query_sport = "hockey".lower().strip()
    query_team = "capitals".lower().strip()

    team_data = get_team_data(query_sport, query_team)
    team_standings = print_team_data(query_sport, query_team, team_data)
    # print()


def get_team_data(query_sport, query_team):
    directory_path = "game_data/" + str(query_sport) + "/"

    # see if we have data
    directory_contents = [
        os.path.splitext(content)[0]
        for content in os.listdir(directory_path)
    ]

    if query_team in directory_contents:
        print("query_team in directory_contents")
        team_data_path = directory_path + query_team + ".json"

        with open(team_data_path) as json_data:
            data = json.load(json_data)

        return list(filter(lambda x:x["game_id"] < 6,data))




def print_team_data(query_sport, query_team, team_data):
    print(json.dumps(team_data, indent=4, sort_keys=True))
    # return (
    #     f"For the sport of {query_sport} the {query_team.capitalize()} last 5 game results are:\n \
    #     {}"
    # )


if __name__ == "__main__":
    main()