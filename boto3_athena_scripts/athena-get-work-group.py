import boto3

client = boto3.client('athena')
response = client.get_work_group(
    WorkGroup='AITeam'
)
print(response)