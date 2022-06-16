import api_key
import boto3
import os
import sys

def main():
	n = len(sys.argv) 

	for arg in sys.argv[1:]:
		print(arg)
if __name__ == "__main__":
    main()