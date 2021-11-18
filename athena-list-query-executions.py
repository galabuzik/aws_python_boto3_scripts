import boto3

client = boto3.client('athena')
response = client.list_query_executions(
    WorkGroup='primary',
    MaxResults=12
)
print(response)