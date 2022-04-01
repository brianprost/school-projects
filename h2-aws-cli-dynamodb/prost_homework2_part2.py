"""
prost_homework2_part2.py
Author: Brian Prost
SDEV 400 7380
"""

import boto3
from boto3.dynamodb.conditions import Attr
import json


def main():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.create_table(
        TableName="CourseCatalog",
        KeySchema=[
            {
                "AttributeName": "CourseID",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "CourseID",
                "AttributeType": "N"
            },
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )

    # wait for table to be available
    print("Creating table. Please wait...")
    table.wait_until_exists()
    print("Table created! Adding data now...")

    # add data to table
    with open('course_catalog.json') as json_data:
        request_items = json.loads(json_data.read())
        for item in request_items:
            table.put_item(Item=item)

    while(True):
        course_subject = get_user_input("Enter the subject:\t\t").upper()
        catalog_number = int(get_user_input("Enter the catalog number:\t"))

        course_title = get_course_title(table, course_subject, catalog_number)
        if not course_title:
            print("No course found. Please try again")
            continue

        print(
            f"The title of {course_subject} {catalog_number} is {course_title}.")

        keep_going = get_user_input(
            "Would you like to search for another title?\t")
        if keep_going[0].lower() == 'n':

            delete_table_confirmation = get_user_input(
                "Would you like to delete the table?\t\t")

            if delete_table_confirmation[0].lower() == 'y':
                table.delete()
                print("Table deleted.")

            print("Goodbye!")
            break


def get_user_input(prompt):
    while True:
        try:
            the_input = input(prompt)
        except ValueError:
            print("Input not accepted. Please try again")
            continue

        if the_input == "":
            print("Nothing entered, please try again.")
            continue
        else:
            break
    return the_input


def get_course_title(table, course_subject, catalog_number):
    response = table.scan(
        FilterExpression=Attr("Subject").eq(course_subject)
        & Attr("CatalogNumber").eq(catalog_number)
    )
    items = response["Items"]
    if len(items) > 0:
        the_item = items[0]
        return the_item["CourseTitle"]
    else:
        return False


if __name__ == '__main__':
    main()
