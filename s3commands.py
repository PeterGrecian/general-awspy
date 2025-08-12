import boto3

"""
imitate aws s3 commands
"""
s3 = boto3.client("s3")
    
def cp(local_file, bucket_name, s3_object_key):
    s3.upload_file(local_file, bucket_name, s3_object_key)

def rm(bucket_name, s3_object_key):
    s3.delete_object(Bucket=bucket_name, Key=s3_object_key)

def ls(bucket_name, debug=False):
    objs = list()
    paginator = s3.get_paginator('list_objects_v2')

    response_iterator = paginator.paginate(Bucket=bucket_name)
    for page in response_iterator:
        for obj in page.get('Contents', []):
            objs.append(obj['Key'])   
    print(f"Objects in {bucket_name}: {objs}")
    return objs      

def cp_back(bucket_name, s3_object_key, local_file):
    s3.download_file(bucket_name, s3_object_key, local_file)

def rm_all(bucket_name):
    objs = ls(bucket_name)
    for obj in objs:
        rm(bucket_name, obj)
