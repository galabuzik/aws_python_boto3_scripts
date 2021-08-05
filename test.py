import boto3

ec2_resource=boto3.resource('ec2')
for resource in ec2_resource.instances.all():
    print(resource)