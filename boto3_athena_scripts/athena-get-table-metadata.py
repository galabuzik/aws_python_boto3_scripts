import boto3

client = boto3.client('athena')
response = client.get_table_metadata(
    CatalogName='AwsDataCatalog',
    DatabaseName='wbc',
    TableName='wbcdata'
)
print(response)