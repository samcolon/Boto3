import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

s3 = session.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': "enter_bucket_name", 'Key': "this_text.txt"}, ExpiresIn=300)

print(response)