""" Function to process the S3 Notification event """
from __future__ import print_function
from random import randint
from time import sleep
import json
import urllib
import re
import boto3
import botocore
import logging
import os


sns_client = boto3.client('sns')
sns_topic_arn = os.environ['TOPIC']

# Setup logging

logger = logging.getLogger()
level = logging.getLevelName('DEBUG')
ENV_LOG_LEVEL = os.getenv('LOG_LEVEL')
if ENV_LOG_LEVEL:
    level = logging.getLevelName(ENV_LOG_LEVEL)
logger.setLevel(level)



def lambda_handler(event, context):
    return_value = ''
    try:
        # Get the object from the event and show its content type
        record = event['Records'][0]['s3']['object']['key']
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        words = record.split("/")
        accountname = words[0]
        message_subject = "Amazon S3 Notification"
        my_event = json.dumps(event)
        return_value = publish_notification(sns_topic_arn, message_subject, my_event)

        logger(return_value)

    except botocore.exceptions.ClientError as e:
        logger.error("Unable to send notification. {}".format(
            e.response["Error"]["Message"]
        ))

def publish_notification(topic_arn, subject, body):
    
    try:
        sns_client.publish(
            TopicArn = topic_arn,
            Subject = subject,
            Message = body
        )
        logger.info("Posted notification to {}".format(topic_arn))
        Return_value = 'Successfully sent notification'
    except botocore.exceptions.ClientError as e:
        logger.error("Unable to send notification. {}".format(
            e.response["Error"]["Message"]
        ))
        Return_value = 'Failed to send notification'
    return Return_value
