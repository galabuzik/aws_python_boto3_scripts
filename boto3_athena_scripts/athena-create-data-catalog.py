import boto3

client = boto3.client('athena')
response = client.create_data_catalog(
    Name='catalog01',
    Type='GLUE',
    Parameters={
        'catalog-id':'585584209241'
    }
)
print(response)