import json
import os


def main():
    # querys
    query_sport = "basketball".lower().strip()
    query_team = "lakers".lower().strip()

    team_data = get_team_data(query_sport, query_team)
    if team_data[0] is "Error.":
        response = [
            team_data[1],
            team_data[2],
            "For more options, please consider upgrading to our Pro Plan. (1 BTC per request)"
        ]
    else:
        response = print_team_data(query_sport, query_team, team_data)
    print(json.dumps(response, indent=4))


def check_if_data_exists(query_sport, query_team, directory_path):
    types_of_sports = [
        os.path.splitext(dir_content)[0]
        for dir_content in os.listdir(directory_path) if not dir_content.startswith(".")
    ]
    if query_sport in types_of_sports:
        sport_teams = [
            os.path.splitext(dir_content)[0]
            for dir_content in os.listdir(directory_path + str(query_sport)) if not dir_content.startswith(".")
        ]
        if query_team in sport_teams:
            return True
        else:
            return ["NO_TEAM", sport_teams]
    else:
        return ["NO_SPORT", types_of_sports]


def get_team_data(query_sport, query_team):
    directory_path = "game_data/"
    there_is_data = check_if_data_exists(
        query_sport, query_team, directory_path)
    if there_is_data is True:
        directory_path += query_sport + "/" + query_team + ".json"

        with open(directory_path) as json_data:
            data = json.load(json_data)

        return list(filter(lambda x: x["game_id"] < 6, data))
    elif there_is_data[0] is "NO_SPORT":
        return ["Error.", f"Sport: {query_sport} was not found. Please try from one of these sports:", there_is_data[1]]
    elif there_is_data[0] is "NO_TEAM":
        return ["Error.", f"Team: {query_team} was not found. Please try from one of these teams:", there_is_data[1]]


def print_team_data(query_sport, query_team, team_data):
    game_log = {
        query_sport: {
            query_team: []
        }
    }
    for game in team_data:
        response = ""
        response += f"{game['date']} - A {query_team.capitalize()}"

        if game['game_won']:
            response += " win against "
        elif not game['game_won']:
            response += " loss to "

        response += f"the {game['opponent']}. The score was {game['points_for']}-{game['points_against']}."

        game_log[query_sport][query_team].append(response)
    return game_log


if __name__ == "__main__":
    main()
