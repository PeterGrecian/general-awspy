# region_names.py
"""
Module for converting between AWS region codes and human-friendly region names.

Public API:
    code_to_name(region_code)  # 'eu-west-1' -> 'Ireland'
    name_to_code(region_name)  # 'Ireland' -> 'eu-west-1'
    get_all_region_codes()     # list of region codes from boto3/AWS CLI
    demo()                    # print all region codes and names
"""

REGION_NAMES = {
    "us-east-1": "N. Virginia",
    "us-east-2": "Ohio",
    "us-west-1": "N. California",
    "us-west-2": "Oregon",
    "af-south-1": "Cape Town",
    "ap-east-1": "Hong Kong",
    "ap-south-1": "Mumbai",
    "ap-south-2": "Hyderabad",
    "ap-southeast-1": "Singapore",
    "ap-southeast-2": "Sydney",
    "ap-southeast-3": "Jakarta",
    "ap-southeast-4": "Melbourne",
    "ap-northeast-1": "Tokyo",
    "ap-northeast-2": "Seoul",
    "ap-northeast-3": "Osaka",
    "ca-central-1": "Canada (Central)",
    "eu-central-1": "Frankfurt",
    "eu-central-2": "Zurich",
    "eu-west-1": "Ireland",
    "eu-west-2": "London",
    "eu-west-3": "Paris",
    "eu-north-1": "Stockholm",
    "eu-south-1": "Milan",
    "eu-south-2": "Spain",
    "me-south-1": "Bahrain",
    "me-central-1": "UAE",
    "sa-east-1": "São Paulo"
}

def code_to_name(region_code):
    """
    Convert AWS region code to friendly name.
    Example: code_to_name('eu-west-1') -> 'Ireland'
    """
    return REGION_NAMES.get(region_code)

def name_to_code(region_name):
    """
    Convert friendly region name to AWS region code.
    Example: name_to_code('Ireland') -> 'eu-west-1'
    """
    for code, name in REGION_NAMES.items():
        if name == region_name:
            return code
    return None

def get_all_region_codes():
    """
    Returns all region codes as reported by AWS using boto3 (needs AWS credentials).
    """
    import boto3
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    return [r['RegionName'] for r in response['Regions']]

def demo():
    print("All regions and their friendly names:")
    for code in get_all_region_codes():
        print(f"{code} => {code_to_name(code)}")
