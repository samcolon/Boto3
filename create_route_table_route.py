import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

route_table_id = 'enter_route_table_id'
internet_gateway_id = 'enter_gateway_id'

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTable_Id=route_table_id,
)