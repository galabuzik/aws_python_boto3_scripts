import boto3, sys
ec2 = boto3.resource('ec2')

ids = ['i-02ddc6a84474ead33']
# Iterate through instance IDs and Terminate Instances
for id in sys.argv[1:]:
    instance = ec2.Instance(id)
    print(instance.terminate())
