import boto3

session = boto3.Session(profile_name='leveluptech')

ec2 = session.client('ec2')

def get_vpc_information(client, filters=[]):
    response = ec2.describe_vpcs(Filters=filters)
    for vpc in response["Vpcs"]:
        print(vpc["VpcId"], vpc["CidrBlock"], vpc["IsDefault"])
        
def get_vpc_name(client, filters=[]):
    response = ec2.describe_vpcs(Filters=filters)
    for vpc in response["Vpcs"]:
        if "Tags" in vpc:
            for tag in vpc["Tags"]:
                if "Name" == tag['key']:
                    print(tag["Value"])
        
                    
Filters=[{'Name': 'isDefault', 'Values': ['true',]},]

get_vpc_information(ec2)
get_vpc_information(ec2, Filters)