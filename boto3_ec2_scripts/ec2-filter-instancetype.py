import boto3  
ec2 = boto3.resource('ec2')  

instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-type', 'Values': ['t2.micro']}])

for instance in instances:
    print(instance.id, instance.instance_type)