# Brian Prost
# upload_covid_data_to_dynamodb.py
import boto3


def main():
    create_db()
    upload_to_db()


def create_db():
    table = boto3.resource("dynamodb").create_table(
        TableName="NytCovidDataDec10",
        KeySchema=[
            {
                "AttributeName": "state",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "state",
                "AttributeType": "S"
            },
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )
    print("Creating table. Please wait...")
    table.wait_until_exists()
    print("Table created! Adding data now...")


def upload_to_db():
    covid_table_dynamodb = boto3.resource(
        'dynamodb').Table('NytCovidDataDec10')
    with open('nyt_us_states.csv', 'r') as f:
        next(f)
        for line in f:
            state, cases, deaths = line.rstrip().split(',')
            covid_table_dynamodb.put_item(
                Item={
                    'state': state,
                    'cases': int(cases),
                    'deaths': int(deaths)
                }
            )
    print("Data added!")


if __name__ == "__main__":
    main()
