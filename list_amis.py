import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

response = ec2.describe_images(Owners=['amazon'])

for image in response["Images"]:
    print(image["ImageId"], image["Name"], image["CreationDate"])