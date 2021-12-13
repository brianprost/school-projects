import boto3
import json
import requests


def menu():
    state_to_lookup = get_state_to_lookup()
    state_covid_data = get_covid_data_for_state(state_to_lookup)
    print_state_covid_data(state_covid_data)


def get_state_to_lookup():
    while True:
        try:
            state_to_lookup = input(
                "Enter a state to lookup it\'s COVID-19 cases & deaths: ")
            with open('us_states.txt', 'r') as us_states:
                if state_to_lookup.lower() in us_states.read():
                    return state_to_lookup
                else:
                    print("State not found. Please try again!")
                    continue
        except ValueError as e:
            print(e.with_traceback())

def get_covid_data_for_state(state_to_lookup):
    api_url = "https://h1589ixccj.execute-api.us-east-1.amazonaws.com/default/CovidDataFunction"
    response = requests.get(api_url, params={"state": state_to_lookup})
    state_covid_data = response.json()
    return state_covid_data['body']


def print_state_covid_data(state_covid_data):
    state = state_covid_data['state']
    cases = state_covid_data['cases']
    deaths = state_covid_data['deaths']

    print(f"As of December 10th, 2021, {state} had {cases:,} cases of COVID-19 and {deaths:,} deaths (New York Times, 2021).")


if __name__ == "__main__":
    menu()
