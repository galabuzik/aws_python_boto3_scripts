import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-02ddc6a84474ead33').stop()
ec2.Instance('i-0f2e7e65198553285').stop()
