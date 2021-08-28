#!/bin/bash

import boto3
BUCKET_NAME = 'lazydinners'
OBJECT_NAME = 'recipes.txt'
FILE_NAME = 'localrecipes.txt'


s3 = boto3.client('s3')
s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')

