import api_key
import boto3
import os
import sys



def main():
	s3_client = boto3.client('s3',
						aws_access_key_id = api_key.aws_key,
						aws_secret_access_key = api_key.aws_secret_key)
	bucket = 'radoslaw-python'
 
	for file in sys.argv[1:]:
		if file in os.listdir():
			object_name = 'data/' + str(file)
			s3_client.upload_file(file, bucket, object_name)
			print("Upload complete")

if __name__ == "__main__":
    main()