import boto3

client = boto3.client('athena')
response = client.create_prepared_statement(
    StatementName='Test_Statement',
    WorkGroup='primary',
    QueryStatement='SELECT * FROM "wbc"."thirdpartydata";',
)
print(response)