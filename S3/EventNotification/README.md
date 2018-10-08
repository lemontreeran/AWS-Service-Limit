Add Permissions to the Lambda Function’s Access Permissions Policy

aws lambda add-permission \
--function-name DocumentProcessor \
--region us-west-2 \
--statement-id allow-s3-to-invoke-lambda123456789 \
--action "lambda:InvokeFunction" \
--principal s3.amazonaws.com \
--source-arn arn:aws:s3:::polyglotdeveloper-user-bucket \
--source-account $AWS_ACCOUNT_ID

{
    "Statement": "{\"Sid\":\"allow-s3-to-invoke-lambda123456789\",\"Resource\":\"arn:aws:lambda:us-west-2:YOUR_ACCOUNT_ID:function:DocumentProcessor\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"s3.amazonaws.com\"},\"Action\":[\"lambda:InvokeFunction\"],\"Condition\":{\"StringEquals\":{\"AWS:SourceAccount\":\"YOUR_ACCOUNT_ID\"},\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:s3:::polyglotdeveloper-user-bucket\"}}}"
}
