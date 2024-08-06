import boto3

client = boto3.client('athena')
response = client.update_data_catalog(
    Name='catalog01',
    Type='GLUE',
    Description='Test environment data catalog',
    Parameters={
        'catalog-id':'585584209241'
    }
)
print(response)