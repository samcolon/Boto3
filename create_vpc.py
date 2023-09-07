import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

vpc = ec2.create_vpc(CidrBlock='12.0.0.0/16')

print(vpc["Vpc"]["VpcId"])