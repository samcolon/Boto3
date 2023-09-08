import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

internet_gateway_id = "enter_gateway_id"

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)