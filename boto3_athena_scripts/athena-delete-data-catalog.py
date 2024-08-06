import boto3

client = boto3.client('athena')
response = client.delete_data_catalog(
    Name='catalog01'
)
print(response)