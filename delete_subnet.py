import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

subnet_id = "enter_subnet_id"

ec2.delete_subnet(
    SubnetId=subnet_id,
)