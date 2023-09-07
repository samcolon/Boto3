import boto3

bucket = "enter_bucketname_here"
key = "enter_key_here"

session = boto3.Session(profile_name='enter_user_profile_here')


s3 = session.client('s3')

response = s3.delete_object(
    Bucket=bucket,
    Key=key
)