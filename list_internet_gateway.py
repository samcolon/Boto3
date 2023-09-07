import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

response = ec2.describe_internet_gateways()

for ig in response["InternetGateways"]:
    print(ig["InternetGatewayId"])
    for attachment in ig["Attachments"]:
        print(attachment["VpcId"], attachment["State"])