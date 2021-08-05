import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
    ImageId='ami-0233c2d874b811deb', #Insert the Amazon Image ID
    MinCount=1, #Minimum number of Instances
    MaxCount=2, #Maximum number of Instances
    InstanceType='t2.micro', #Set the EC2 Instance type
    KeyName='ssh-keypair' #Insert the Key Pair Name
)
