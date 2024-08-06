import boto3

client = boto3.client('athena')
response = client.list_data_catalogs()
print(response)