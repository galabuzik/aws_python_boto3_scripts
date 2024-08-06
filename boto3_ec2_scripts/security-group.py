import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
   response = ec2.describe_security_groups(GroupIds=['sg-05ffad71ec1b899b5','sg-0a1882cd57bbf2ac1'])
   print(response)
except ClientError as e:
    print(e)
