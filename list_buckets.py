import boto3

session = boto3.Session(profile_name='enter_profile_name_here')

s3 = session.client('s3')

response = s3.list_buckets()

buckets = response['Buckets']

for bucket in buckets:
    print(bucket["Name"], bucket["CreationDate"])
