import boto3
import os
import datetime
import logging
from logging.config import fileConfig

# Configure logging
fileConfig('logging.ini')
logger = logging.getLogger('dev')

def create_aws_session(profile_name):
    try:
        session = boto3.Session(profile_name=profile_name)
        s3 = session.client('s3')
        logger.warning(f"AWS session: {s3}")
        return s3
    except Exception as e:
        logger.error(f"Error creating AWS session: {e}")
        return None

def generate_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def upload_to_s3(s3, local_folder, bucket_name, s3_prefix):
    timestamp = generate_timestamp()
    s3_prefix_with_timestamp = f'{s3_prefix}/'

    for file_name in os.listdir(local_folder):
        local_file_path = os.path.join(local_folder, file_name)
        if os.path.isfile(local_file_path):
            s3_key = f'{s3_prefix_with_timestamp}{file_name}'

            try:
                #s3.head_object(Bucket=bucket_name, Key=s3_key)
                s3.upload_file(local_file_path, bucket_name, s3_key)
                logger.info(f'Uploaded {local_file_path} to S3 bucket {bucket_name} with key {s3_key}')
            except Exception as e:
                logger.error(f'Error uploading file: {e}')


    logger.info('All files uploaded to S3')

def main():
    aws_profile = 'private1'
    bucket_name = 'nebotask-test-data'
    s3_prefix = 'folder/'
    local_folder = 'd://s3/'

    s3 = create_aws_session(aws_profile)
    if s3 is None:
        exit(1)

    upload_to_s3(s3, local_folder, bucket_name, s3_prefix)

if __name__ == '__main__':
    main()
