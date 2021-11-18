import boto3

client = boto3.client('athena')
response = client.list_tags_for_resource(
    ResourceARN='arn:aws:athena:us-east-2:585584209241:workgroup/primary'
)
print(response)