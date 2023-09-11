import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"], instance["InstanceType"],
        instance["ImageId"], instance["VpcId"], instance["SubnetId"],
        instance["State"]["Name"])
        
        if "Tags" in instance:
            for tag in instance["Tags"]:
                if tag["Key"] == "Name":
                    print(tag["Value"])
                    
        for sg in instance["SecurityGroups"]:
            print(sg["GroupId"], sg["Groupname"])
            
        if "PublicIPAddress" in instance:
           print(instance["PublicIPAddress"])
           
        if "KeyName" in instance:
           print(instance["KeyName"])
           
        if "IamInstanceProfile" in instance:
            print(instance["IamInstanceProfile"]["Id"], instance["IamInstanceProfile"]["Arn"])