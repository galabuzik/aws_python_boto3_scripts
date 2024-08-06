import boto3

ec2 = boto3.resource('ec2')
ids = ['i-02ddc6a84474ead33']

ec2.instances.filter(InstanceIds=ids).stop()
response = ec2.instances.filter(InstanceIds=ids).terminate()
print(response)

