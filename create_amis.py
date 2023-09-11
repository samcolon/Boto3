import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

response = ec2.create_image(
    InstanceId= 'enter_image_Id',
    Name='Go to Ami'
)

print(response["ImageId"])