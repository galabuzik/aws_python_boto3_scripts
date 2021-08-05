import boto3

sts_client = boto3.client('sts')

assumed_role_object=sts_client.assume_role(
    RoleArn="arn:aws:iam::585584209241:user/ec2-testuser",
    RoleSessionName="Session1"
)

credentials=assumed_role_object['Credentials']

ec2_resource=boto3.resource(
    'ec2',
    aws_access_key_id=credentials['AKIAYQV4J5VMYSZXT6HO'],
    aws_secret_access_key=credentials['rkbRJrGFvB+ZXwBJXTKWCiSESc/Ip0iaWWK4KqOi'],
    aws_session_token=credentials['Insert-Session-Your-Token-Here'],
)

for resource in ec2_resource.instances.all():
    print(resource)