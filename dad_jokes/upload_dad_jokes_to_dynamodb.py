import boto3


def main():
    create_db()
    upload_to_db()


def create_db():
    table = boto3.resource("dynamodb").create_table(
        TableName="DadJokesDb",
        KeySchema=[
            {
                "AttributeName": "joke_id",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "joke_id",
                "AttributeType": "N"
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
    dad_joke_table_dynamodb = boto3.resource('dynamodb').Table('DadJokesDb')
    with open('dad_jokes.csv', 'r') as f:
        next(f)
        for joke in f:
            joke_id, joke = joke.rstrip().split(',')
            dad_joke_table_dynamodb.put_item(
                Item={
                    'joke_id': int(joke_id),
                    'joke': joke
                }
            )
    print("Data added!")


if __name__ == "__main__":
    main()
