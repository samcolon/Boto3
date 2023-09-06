import boto3

session = boto3.Session(profile_name='enter_profile_name_here')

s3 = session.client('s3')

response = s3.list_objects_v2(Bucket="enter_bucket_name_here")

for content in response["Contents"]:
    if(".txt" in content["Key"]):
     print(content["Key"])