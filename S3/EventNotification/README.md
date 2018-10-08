
## Add Lambda Execution Role
$ aws iam create-role \
--role-name S3Event-lambda-execution-role \
--assume-role-policy-document  file://config/policies/s3-lambda-notification-trustpolicy.json.json

## Add Permissions to the Lambda Function’s Access Permissions Policy

$ aws lambda add-permission \
--function-name CloudtrailMonitor \
--region region \
--statement-id some-unique-id \
--action "lambda:InvokeFunction" \
--principal s3.amazonaws.com \
--source-arn arn:aws:s3:::sourcebucket \
--source-account bucket-owner-account-id \
--profile adminuser

```
{  
   "Statement":{  
      "Sid":"allow-s3-to-invoke-lambda123456789",
      "Resource":"arn:aws:lambda:us-west-2:LAMBDA_OWNER_ACCOUNT_ID:function:CloudtrailMonitor",
      "Effect":"Allow",
      "Principal":{  
         "Service":"s3.amazonaws.com"
      },
      "Action":[  
         "lambda:InvokeFunction"
      ],
      "Condition":{  
         "StringEquals":{  
            "AWS:SourceAccount":"S3_OWNER_ACCOUNT_ID"
         },
         "ArnLike":{  
            "AWS:SourceArn":"arn:aws:s3:::CloudtrailMonitor"
         }
      }
   }
}
```
## Add Permissions to the SNS 
    "Statement": "{\"Condition\":{\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:lambda:us-east-1:B:function:SNS-X-Account\"}},\"Action\":[\"lambda:InvokeFunction\"],\"Resource\":\"arn:aws:lambda:us-east-1:A:function:SNS-X-Account\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"sns.amazonaws.com\"},\"Sid\":\"sns-x-account1\"}"

