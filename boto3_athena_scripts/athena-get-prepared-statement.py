import boto3

client = boto3.client('athena')
response = client.get_prepared_statement(
    StatementName='Test_Statement',
    WorkGroup='primary'
)
print(response)