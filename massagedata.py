#!python

import boto3
import random
import json

my_bucket = 'lazydinners'
my_key = 'allrecipes.json'

s3 = boto3.client('s3')

object = s3.get_object(Bucket = my_bucket, Key = my_key)
object_data = json.loads(object['Body'].read())

data = []
data += object_data




