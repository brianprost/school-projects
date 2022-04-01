# Brian Prost
# covid_lambda_function.py
import boto3
import json


def lambda_handler(event, context):
    dynamodb_r = boto3.resource('dynamodb')
    covid_data_table = dynamodb_r.Table('NytCovidDataDec10')
    state_to_lookup = event['state']
    state_covid_data = get_covid_data_for_state(
        covid_data_table, state_to_lookup)
    # state_cases, state_deaths = state_covid_data['cases'], state_covid_data['deaths']

    return {
        'statusCode': 200,
        'body': state_covid_data
    }


def get_covid_data_for_state(covid_data_table, state_to_lookup):
    response = covid_data_table.get_item(
        Key={'state': state_to_lookup.title()})
    state_covid_data = response['Item']
    return state_covid_data
