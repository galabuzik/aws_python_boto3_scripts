import boto3

client = boto3.client('athena')

response = client.list_named_queries(
    MaxResults=10,
    WorkGroup='primary'
)
print(response)