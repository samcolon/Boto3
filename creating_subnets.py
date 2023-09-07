import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

cidr_block = '12.0.1.0/24'
vpc_id = 'enter_vpc_id_here'

subnet = ec2.create_subnet(CidrBlock=cidr_block,VpcId=vpc_id)

print(subnet["Subnet"]["SubnetId"])