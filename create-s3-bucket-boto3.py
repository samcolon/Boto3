import boto3

session = boto3.Session(profile_name='enter_profile_here')

s3 = session.client('s3')

response = s3.create_bucket(Bucket='enter_unique_bucket_name_here')

print(response)