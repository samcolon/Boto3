import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

s3 = session.client('s3')

bucket = "enter_bucketname_here"
Key = "enter_filename_here"

# make bucket public
response = s3.put_public_access_block(
    Bucket=bucket,
   
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }  
)
response = s3.put_bucket_ownership_controls(
    Bucket=bucket,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'
            },
        ]
    }
)

response = s3.put_bucket_acl(
    ACL='private',
    Bucket=bucket)
    
response = s3.put_object_acl(ACL='public-read',
                             Bucket=bucket,
                             Key=Key)

print(response)