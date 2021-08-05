import boto3  

ec2 = boto3.resource('ec2')
ec2_tag={'Name': 'tag:Environment', 'Values': ['Test']}
for instance in ec2.instances.filter(Filters=[ec2_tag]):
 print (instance.id)
