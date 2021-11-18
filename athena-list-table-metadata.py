import boto3

client = boto3.client('athena')
response = client.list_table_metadata(
    CatalogName='AwsDataCatalog',
    DatabaseName='wbc',
)
print(response)