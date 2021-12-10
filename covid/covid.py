import json


def menu():
    # TODO: move to DynamoDB
    with open('covid/nyt_us_states.json') as f:
        covid_db = json.load(f)

    while True:
        try:
            state_to_lookup = input(
                "Enter a state to lookup it's COVID-19 cases & deaths: ")
            with open('covid/us_states.txt', 'r') as us_states:
                if state_to_lookup.lower() in us_states.read():
                    print(f"{state_to_lookup} found!")
                    break
                else:
                    print("State not found. Please try again!")
                    continue

        except ValueError as e:
            print(e.with_traceback(tb))


if __name__ == "__main__":
    menu()
