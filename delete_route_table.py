import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

route_table_id = "enter_route_table_id"

ec2.delete_route_table(
    RouteTableId=route_table_id,
)