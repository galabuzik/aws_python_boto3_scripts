import boto3

client = boto3.client('athena')

response = client.get_named_query(
    NamedQueryId='b1fc5c6e-cd83-451e-b69f-6d7b1ae73795'
)
print(response)