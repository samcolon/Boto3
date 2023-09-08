import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

internet_gateway_id = 'enter_gateway_ID'
vpc_id = 'enter_VPC ID'

ec2.attach_internet_gateway(
    InternetGatewayID=internet_gateway_id,
    VpcId=vpc_id
)