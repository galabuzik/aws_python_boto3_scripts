import boto3

client = boto3.client('athena')
response = client.list_engine_versions()
print(response)