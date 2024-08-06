import boto3

client = boto3.client('athena')
response = client.list_prepared_statements(
    WorkGroup='primary',
)
print(response)