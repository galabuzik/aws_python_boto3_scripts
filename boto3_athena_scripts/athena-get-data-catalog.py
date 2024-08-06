import boto3

client = boto3.client('athena')
response = client.get_data_catalog(
    Name='catalog01'
)
print(response)