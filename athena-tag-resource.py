import boto3

client = boto3.client('athena')
response = client.tag_resource(
    ResourceARN='arn:aws:athena:us-east-2:585584209241:workgroup/primary',
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Test'
        },
    ]
)
print(response)