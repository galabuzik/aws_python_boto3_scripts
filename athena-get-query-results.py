import boto3

client = boto3.client('athena')
response = client.get_query_results(
    QueryExecutionId='da20d77e-b714-465f-a98f-b3586da66585',
    MaxResults=10
)
print(response)