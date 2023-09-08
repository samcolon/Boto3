import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

vpc_id = "enter_vpc_id"

ec2.delete_vpc(
    VpcId=vpc_id,
)