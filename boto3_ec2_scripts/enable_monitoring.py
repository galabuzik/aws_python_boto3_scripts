import sys
import boto3

ec2 = boto3.client('ec2')
if sys.argv[0] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['i-02ddc6a84474ead33'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-02ddc6a84474ead33'])
print(response)