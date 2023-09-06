import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

s3 = session.client('s3')

with open("this_text.txt", 'rb') as f:
    s3.put_object(Bucket="enter_bucket_name", Key='this_text.txt', Body=f, ContentType="text/plain")
    
###This is the command for adding a file path###

#s3.upload_file('filename', 'bucketname', 'Key', ExtraArgs={"0ContentType':'text/plain'})