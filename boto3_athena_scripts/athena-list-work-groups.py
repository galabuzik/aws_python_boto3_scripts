import boto3

client = boto3.client('athena')
response = client.list_work_groups()
print(response)