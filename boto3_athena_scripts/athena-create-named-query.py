import boto3

client = boto3.client('athena')

response = client.create_named_query(
    Name='TestQuery',
    Database='wbc',
    QueryString='SELECT * FROM "wbc"."thirdpartydata" limit 10;',
)
print(response)