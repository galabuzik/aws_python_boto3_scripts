import boto3

client = boto3.client('athena')
response = client.stop_query_execution(
    QueryExecutionId='da20d77e-b714-465f-a98f-b3586da66585'
)
print(response)