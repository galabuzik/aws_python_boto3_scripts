import boto3

client = boto3.client('athena')
response = client.update_work_group(
    WorkGroup='AITeam',
    ConfigurationUpdates={
        'ResultConfigurationUpdates': {
            'OutputLocation': 's3://wbc-card-data01/',
            }
    }
)
print(response)