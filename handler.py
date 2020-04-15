import boto3

client = boto3.client('sts')

def handler(event, context):
    response = client.get_caller_identity()

    message = 'Hello {}!'.format(response['UserId'])  

    return { 
        'message' : message
    }