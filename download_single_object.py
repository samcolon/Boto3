import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

bucket = 'enter_bucketname_here'
key = 'enter_key_here'
filename = 'enter_filename_here'

s3 = session.client('s3')

# downloads one file
def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename )
