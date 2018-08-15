import boto3
import json

def lambda_handler(event, context):
    # Given user data save in dynamoDB
    client = boto3.client('dynamodb')
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
