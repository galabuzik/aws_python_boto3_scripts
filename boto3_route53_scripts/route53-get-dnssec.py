import boto3

client = boto3.client('route53')
response = client.get_dnssec(
    HostedZoneId='Z00594533FY3S68ROG6V2'
)
print(response)