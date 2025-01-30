import boto3
import json

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    
    # Check if the stop was manual
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state_reason = response['Reservations'][0]['Instances'][0].get('StateReason', {}).get('Message', '')

    # If the stop was manual, exit
    if "User initiated" in state_reason:
        return {
            'statusCode': 200,
            'body': f'Instance {instance_id} was manually stopped. No action taken.'
        }

    # Start the instance only if it wasn't manually stopped
    ec2.start_instances(InstanceIds=[instance_id])
    
    return {
        'statusCode': 200,
        'body': f'Instance {instance_id} has been restarted.'
    }
