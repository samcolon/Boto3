import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ami_id = "enter_ami_id"
key_pair_name = "enter_keypair_name"
security_group_id = "enter_security_group"
ec2 = session.client('ec2')

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        security_group_id
    ]
)

print(response["Instances"][0]["InstanceId"])