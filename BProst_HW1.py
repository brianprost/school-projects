import boto3
import botocore
import datetime
import random
import math
from simple_term_menu import TerminalMenu

def main():
    s3 = boto3.client('s3')
    menu()
    
    
def create_bucket():
    
    # generate name for bucket
    digits = [i for i in range(0, 10)]
    random_digits = ""
    
    for i in range(6):
        index = math.floor(random.random() * 10)
        random_digits += str(digits[index])
        
    new_bucket_name = ("brianprost-" + random_digits)
    
    # create the bucket
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=new_bucket_name)
    
    # set access constraints
    s3.put_public_access_block(
        Bucket=new_bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        },
    )
    
    print("Created a new bucket called: " + new_bucket_name)


def put_object_in_bucket():
    s3 = boto3.client('s3')
    file_to_upload = 'README.md'
    bucket_to_upload_to = 'bprost.homework1.bucket2'
    s3.upload_file(file_to_upload, bucket_to_upload_to, file_to_upload)


def delete_object_from_bucket():
    s3 = boto3.client('s3')
    bucket_to_delete_from = 'edu.umgc.florida.info'
    object_to_delete = 'iu-15.jpeg'
    s3.delete_object(Bucket=bucket_to_delete_from, Key=object_to_delete)
    print("Deleted 'iu-15.jpeg' from Florida Info bucket.")


def delete_a_bucket():
    s3 = boto3.client('s3')
    list_current_buckets()
    bucket_to_delete = input("Please type the name of the bucket you would like to delete:\n")
    s3.delete_bucket(Bucket=bucket_to_delete)
    print("Deleted bucket: " + bucket_to_delete)


def copy_object_from_another_bucket():
    s3 = boto3.client('s3')
    bucket_source_name = 'bprost.homework1.bucket2'
    object_name = 'johncenaintro.wav'
    copy_this_object = {
        'Bucket': bucket_source_name,
        'Key': object_name
    }
    s3.copy_object(CopySource = copy_this_object, Bucket = 'bprost.homework1.bucket1', Key = object_name)


def download_object_from_bucket():
    s3 = boto3.resource('s3')
    s3.Bucket('bprost.homework1.bucket1').download_file('jobs/pic 2.jpeg','file.jpeg')
    

def application_exit():
    date_and_time = datetime.datetime.now()
    print("Thanks for messing with my data!")
    print("BTW, the current time and date is:" + date_and_time.strftime("%Y-%m-%d %H:%M:%S"))
    
    
def list_current_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("Current Buckets: %s" % buckets)


def menu():
    print("Welcome to our introduction to S3.\n")
    menu_options = ["Create an S3 bucket consiting of my name and a random 6 digit suffix.", "Put objects in a previously created bucket", "Delete an object in a bucket", "Delete a bucket", "Copy an object from one bucket to another", "Download an existing object from a bucket", "Exit"]
    terminal_menu = TerminalMenu(menu_options, title="Which of the following would you like to do?", menu_cursor_style=("fg_green", "bold"), menu_highlight_style=("bg_green", "fg_black"))
    user_action_choice = terminal_menu.show()
    print(f"You have selected:\t {menu_options[user_action_choice]}!\n")
    
    if (user_action_choice == 0):
        create_bucket()
    elif (user_action_choice == 1):
        put_object_in_bucket()
    elif (user_action_choice == 2):
        delete_object_from_bucket()
    elif (user_action_choice == 3):
        delete_a_bucket()
    elif (user_action_choice == 4):
        copy_object_from_another_bucket()
    elif (user_action_choice == 5):
        download_object_from_bucket()
    elif (user_action_choice == 6):
        application_exit()



if __name__ == '__main__':
    main()
    