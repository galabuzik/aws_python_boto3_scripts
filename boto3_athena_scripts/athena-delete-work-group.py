import boto3

client = boto3.client('athena')
response = client.delete_work_group(
    WorkGroup='AITeam',
    RecursiveDeleteOption=True
)
print(response)