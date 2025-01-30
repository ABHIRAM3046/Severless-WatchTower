import boto3

def lambda_handler(event, context):
    elbv2 = boto3.client('elbv2')
    target_group_arn = event['detail']['targetGroupArn']
    response = elbv2.describe_target_health(TargetGroupArn=target_group_arn)
    
    unhealthy_targets = [
        target['Target']['Id']
        for target in response['TargetHealthDescriptions']
        if target['TargetHealth']['State'] != 'healthy'
    ]
    
    for target in unhealthy_targets:
        elbv2.deregister_targets(TargetGroupArn=target_group_arn, Targets=[{'Id': target}])
        print(f"Deregistered unhealthy target {target}.")
