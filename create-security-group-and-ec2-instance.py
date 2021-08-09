import boto3
from botocore.exceptions import ClientError


class CreateInstanceEC2(object):
    def __init__(self, ec2_client):
        self.ec2_client = ec2_client

    def grep_vpc_subnet_id(self):
        response = self.ec2_client.describe_vpcs()
        for vpc in response["Vpcs"]:
            if vpc["Tags"][0]["Value"].__contains__("Default"):
                vpc_id = vpc["VpcId"]
                break
        print("The Default VPC : ", vpc_id)
        response = self.ec2_client.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
        subnet_id = response["Subnets"][0]["SubnetId"]
        print("The Default Subnet : ", subnet_id)
        return vpc_id, subnet_id

    def create_security_group(self):
        sg_name = "https_security_group"
        try:
            vpc_id, subnet_id = self.grep_vpc_subnet_id()
            response = self.ec2_client.create_security_group(
                GroupName=sg_name,
                Description="Allow HTTPS Traffic",
                VpcId=vpc_id
            )
            sg_id = response["GroupId"]
            print(sg_id)
            sg_config = self.ec2_client.authorize_security_group_ingress(
                GroupId=sg_id,
                IpPermissions=[
                    {
                        'IpProtocol':'tcp',
                        'FromPort':443,
                        'ToPort': 443,
                        'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
                    }
                ]
            )
            print(sg_config)
            return sg_id, sg_name
        except Exception as e:
            if str(e).__contains__("already exists"):
                response = self.ec2_client.describe_security_groups(GroupNames=[sg_name])
                sg_id = response["SecurityGroups"][0]["GroupId"]
                print(sg_id, sg_name)
                return sg_id, sg_name

    def create_ec2_instance(self):
        
        print("Creating EC2 instance")
        sg_id, sg_name = self.create_security_group()
        vpc_id, subnet_id = self.grep_vpc_subnet_id()
        self.ec2_client.run_instances(
            ImageId="ami-0233c2d874b811deb",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="ssh-keypair",
            SecurityGroupIds=[sg_id],
            SubnetId=subnet_id,
        )

try:
    ec2_client = boto3.client('ec2')
    call_obj = CreateInstanceEC2(ec2_client)
    call_obj.grep_vpc_subnet_id()
    call_obj.create_security_group()
    call_obj.create_ec2_instance()
except ClientError as e:
    print("There is a error in the client configuration: ", e)
