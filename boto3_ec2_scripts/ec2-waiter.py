import boto3

ec2 = boto3.client('ec2')
waiters = ec2.waiter_names
print(waiters)

