import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

ig = ec2.create_internet_gateway()

print(ig["InternetGateway"]["InternetGatewayId"])