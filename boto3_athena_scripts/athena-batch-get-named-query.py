import boto3

client = boto3.client('athena')
response = client.batch_get_named_query(
    NamedQueryIds=[
        '9a09d73c-6a9a-4b86-8c33-1ecc68e161de',
        '1dc56214-96e0-47ef-8944-1882c4043da2'
    ]
)
print(response)