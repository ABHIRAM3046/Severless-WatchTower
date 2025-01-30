import boto3

s3 = boto3.client('s3')
BACKUP_BUCKET = "global-backup-bucket"

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        s3.copy_object(
            Bucket=BACKUP_BUCKET,
            CopySource={'Bucket': bucket, 'Key': key},
            Key=f"{bucket}/{key}"
        )
        print(f"Backed up {key} from {bucket} to {BACKUP_BUCKET}.")
