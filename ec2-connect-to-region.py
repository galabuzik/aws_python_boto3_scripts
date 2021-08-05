import boto3

ec2 = boto3.client('ec2')

ags_west = boto3.setup_default_session(region_name='us-east-2')

print(ags_west)

