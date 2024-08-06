import boto3

def get_security_groups(self, vpc=None):

        sec_groups_all_keys = [
            'IpPermissionsEgress',
            'Description',
            'GroupName',
            'VpcId',
            'OwnerId',
            'GroupId',
        ]

        if vpc is None:
            try:
                response = self.client_ec2.describe_security_groups()
            except Exception as e:
                raise ValueError(e)
        else:
            try:
                response = self.client_ec2.describe_security_groups( Filters=[{'Name': 'vpc-id', 'Values': [vpc]}] )
            except Exception as e:
                raise ValueError(e)

        return response['SecurityGroups']