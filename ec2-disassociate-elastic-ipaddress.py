import boto3

ec2 = boto3.client('ec2')

response = ec2.disassociate_address(
    PublicIp='3.132.166.13',
)

print(response)