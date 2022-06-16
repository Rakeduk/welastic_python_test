import api_key
import boto3
import os
import sys
from botocore.exceptions import ClientError


def main():
    s3_client = boto3.client('s3',
                             aws_access_key_id=api_key.aws_key,
                             aws_secret_access_key=api_key.aws_secret_key)
    bucket = 'radoslaw-python'

    for file in sys.argv[1:]:
        if file in os.listdir():
            object_name = 'data/' + file
            try:
                s3_client.upload_file(file, bucket, object_name)
                print(f"{file} uploaded")
            except ClientError as e:
            	print(f"Upload of {file} not completed")


if __name__ == "__main__":
    main()
