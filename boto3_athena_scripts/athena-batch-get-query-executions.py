import boto3

client = boto3.client('athena')
response = client.batch_get_query_execution(
    QueryExecutionIds=[
        '3a427d8f-2582-49b5-a752-1d87b8fe9107',
        'f395e1f6-4a68-4ead-bb8d-cb7064a12341'
    ]
)
print(response)