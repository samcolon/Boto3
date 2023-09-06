import boto3

session = boto3.Session(profile_name='leveluptech')

s3 = session.client('s3')

with open("this_text.txt", 'rb') as f:
    s3.put_object(Bucket="levelup0923123456", Key='this_text.txt', Body=f, ContentType="text/plain")
    
###This is the command for adding a file path###

#s3.upload_file('filename', 'bucketname', 'Key', ExtraArgs={"0ContentType':'text/plain'})