import boto3

client = boto3.client('athena')
response = client.update_prepared_statement(
    StatementName='Test_Statement',
    WorkGroup='primary',
    QueryStatement='SELECT * FROM "wbc"."wbcdata";',
)
print(response)