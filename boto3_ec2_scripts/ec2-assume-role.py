import boto3

sts_client = boto3.client('sts')

assumed_role_object=sts_client.assume_role(
    RoleArn="arn:aws:iam::XXXXXXXXXXXX:user/ec2-testuser",
    RoleSessionName="Session1"
)

credentials=assumed_role_object['Credentials']

ec2_resource=boto3.resource(
    'ec2',
    aws_access_key_id=credentials['Insert-key-id-here'],
    aws_secret_access_key=credentials['Insert-secret-access-key-here'],
    aws_session_token=credentials['Insert-session-token-here'],
)

for resource in ec2_resource.instances.all():
    print(resource)
