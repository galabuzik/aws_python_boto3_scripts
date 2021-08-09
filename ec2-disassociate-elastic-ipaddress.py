import boto3

ec2 = boto3.client('ec2')

response = ec2.disassociate_address(
    PublicIp='Insert-public-Ipv4-address-here',
)

print(response)
