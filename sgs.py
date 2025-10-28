import boto3

# CIDR ranges and their descriptions
cidr_ranges = {
    "10.8.67.0/24": "Jburg 10.8.67.0/24 Voice Trust SIP Signaling - VLAN 22",
    "10.7.35.0/24": "miami",
    "10.7.3.0/24": "culpeper VLAN 22 - Voice Trust SIP Signaling",
    "10.8.83.0/24": "southafrica Voice Trust SIP Signaling - VLAN 22"
}

def get_regions():
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    return [region['RegionName'] for region in response['Regions']]

def get_security_groups(region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances(
        Filters=[{'Name': 'tag:Name', 'Values': ['*med*']}]
    )
    sg_names = set()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            for sg in instance.get('SecurityGroups', []):
                sg_names.add(sg['GroupId'])
    return list(sg_names)

def add_ingress_rule(region, group_id, cidr_ip, description):
    ec2 = boto3.client('ec2', region_name=region)
    try:
        ec2.authorize_security_group_ingress(
            GroupId=group_id,
            IpPermissions=[
                {
                    'IpProtocol': '-1',
                    'IpRanges': [
                        {
                            'CidrIp': cidr_ip,
                            'Description': description
                        }
                    ]
                }
            ]
        )
        print(f"Added rule to {group_id} in {region} for {cidr_ip}")
    except Exception as e:
        print(f"Failed to add rule to {group_id} in {region} for {cidr_ip}: {e}")

def main():
    regions = get_regions()
    for region in regions:
        print(f"Processing region: {region}")
        sg_ids = get_security_groups(region)
        for sg_id in sg_ids:
            for cidr_ip, description in cidr_ranges.items():
                add_ingress_rule(region, sg_id, cidr_ip, description)

if __name__ == "__main__":
    main()
