import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.associate_address(InstanceId='i-037b17c0fb68072cd',
                                     AllocationId='eipalloc-0fd6f99e439a12903')
    print(response)
except ClientError as e:
    print(e)