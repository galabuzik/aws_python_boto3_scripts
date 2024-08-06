import boto3

client = boto3.client('athena')
response = client.untag_resource(
    ResourceARN='arn:aws:athena:us-east-2:585584209241:workgroup/primary',
    TagKeys=[
        'Environment',
    ]
)
print(response)