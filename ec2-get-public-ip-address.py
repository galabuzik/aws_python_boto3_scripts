import boto3

client = boto3.client('ec2')

response = client.describe_instances()
block_mappings = (Network
                  for reservation in response["Reservations"]
                  for instance in reservation["Instances"]
                  for Network in instance["NetworkInterfaces"])

for Network in block_mappings:
  print(Network["Association"]["PublicIp"])