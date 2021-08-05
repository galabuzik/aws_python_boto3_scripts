import boto3

client = boto3.client('ec2')
addr = client.allocate_address(Domain='vpc')
print (addr['PublicIp'])