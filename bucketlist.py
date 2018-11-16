import boto3
s3 = boto3.client('s3')
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print ("Buckets: %s" % buckets)
s3.create_bucket(Bucket = 'vinotest02', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
print("Buckets: %s" % buckets)

