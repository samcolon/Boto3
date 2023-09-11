import boto3
import os

key_name = "Key from boto3"
file_name = 'key-from-boto3.pem'

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

response = ec2.create_key_pair(
    KeyName=key_name,
)

with open(file_name, 'w') as f:
    f.write(response["keymaterial"])
    
os.chmod(file_name, 0o400)