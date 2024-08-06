import boto3

ec2 = boto3.resource('ec2')

instances = ec2.instances.all()

tag = []

tagtest = {}

tagtest ['Key'] = 'Environment'
tagtest['Value'] = 'Test'

tag.append(tagtest)

for instance in instances:
    instance.create_tags(Tags=tag)
    
for instance in instances:
    print(instance.tags)
    