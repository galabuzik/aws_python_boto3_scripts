import boto3

instance_id = 'i-07816a073fd00c08d'
ec2 = boto3.client('ec2')
response = ec2.describe_instances(InstanceIds=[instance_id])
print(response)