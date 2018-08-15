import boto3
import json

'''
This lambda takes a json describing the user and checks if a duplicate one already exists based on the email.
It returns status code 200 if the table does not contain duplicates and returns status code 400 if such a user exists with the same information.
'''

def lambda_handler(event, context):
    # Given user data save in dynamoDB
    client = boto3.client('dynamodb')
    response = client.get_item(TableName='Technica-Data',Key={'email':{'S':event['email']}})
    if 'Item' in response:
        raise Exception('Invalid input: user already exists.')
    response = client.put_item(TableName='Technica-Data',Item={
        'email':{'S':event['email']},
        'first_name':{'S':event['first_name']},
        'last_name':{'S':event['last_name']},
        'minor_status':{'BOOL':event['minor_status']},
        'organizer':{'BOOL':event['organizer']},
        'other':{'S':event['other']},
        'phone':{'S':event['phone']},
        'shirt_size':{'S':event['shirt_size']},
        'university':{'S':event['university']},
        'dietary_restrictions':{'SS':event['dietary_restrictions']}})
    return {"statusCode": 200, \
        "headers": {"Content-Type": "application/json"}, \
        "body": response}
