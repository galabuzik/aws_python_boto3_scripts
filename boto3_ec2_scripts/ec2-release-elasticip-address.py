import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')

try:
    response = ec2.release_address(AllocationId='eipalloc-0dde2f66e2a386d96')
    print('Address released')
except ClientError as e:
    print(e)