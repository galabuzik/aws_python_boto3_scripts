import boto3

client = boto3.client('athena')
response = client.create_work_group(
    Name='AITeam',
    Configuration={
        'ResultConfiguration': {
            'OutputLocation': 's3://aiteam01/'
        }
    }
)
print(response)