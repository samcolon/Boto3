import boto3

session = boto3.Session(profile_name='enter_user_profile_here')

ec2 = session.client('ec2')

route_table_id = "enter_route_table_id"

response = ec2.describe_route_tables(
    RouteTableIds=[
        route_table_id
    ],
)

for association in response["RouteTables"][0]["Associations"]:
    if not association["Main"]:
        association_id = association["RouteTableAssociationId"]
        print(association_id)
        ec2.disassociate_route_table(
            AssociationId=association_id,
        )