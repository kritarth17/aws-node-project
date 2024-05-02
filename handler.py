import json
import boto3
from io import BytesIO
from PIL import Image, ImageOps
import os
import uuid

s3 = boto3.client('s3')
size = int(os.environ['THUMBNAIL_SIZE'])


def s3_thumbnail_generator(event, context):
    #parse event
    print("EVENT:::", event)
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
