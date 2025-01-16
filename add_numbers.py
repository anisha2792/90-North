def lambda_add_numbers(event, context):
         num1, num2 = event['num1'], event['num2']
         return {"result": num1 + num2}

import boto3

def lambda_store_file(event, context):
         s3 = boto3.client('s3')
         file_content, bucket_name, file_name = event['file_content'], event['bucket_name'], event['file_name']
         s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
         return {"message": "File stored successfully!"}