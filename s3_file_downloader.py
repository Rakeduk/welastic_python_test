import api_key
import boto3
import sys
import botocore


def main():
    s3_client = boto3.client('s3',
                             aws_access_key_id=api_key.aws_key,
                             aws_secret_access_key=api_key.aws_secret_key)
    bucket = 'radoslaw-python'

    for file in sys.argv[1:]:
        file_name = 'data/' + file
        object_name = file
        try:
            s3_client.download_file(bucket, file_name, object_name)
            print(f"{object_name} downloaded")
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not esist")
            else:
                raise


if __name__ == "__main__":
    main()
