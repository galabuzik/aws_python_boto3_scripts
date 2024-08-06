import boto3

client = boto3.client('athena')
response = client.start_query_execution(
    QueryString='SELECT * FROM "wbc"."wbcdata";',
    QueryExecutionContext={
        'Database': 'wbc'
    },
     ResultConfiguration={
        'OutputLocation': 's3://aws-athena-query-results-wbc01/',
        },
    WorkGroup='primary'
)
print(response)