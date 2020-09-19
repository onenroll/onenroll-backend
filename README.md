# onenroll-reviews-backend
This is REST API which was design primarily to handle GET and POST request for reviews module of oneroll

This last updated Version successfully deployed on AWS lambda and handles all incoming GET Request.

All static files and incoming media files(here pictures) are handled and stored successfully on AWS S3

POST Development is not fully-functional and tested. So may not fully work


#Deployment of Django and PostgreSQL using Zappa on Lambda

Install zappa in virtual Env using pip zappa 

Install psycopg2-binary instead of psycopg2 or else Zappa 0.51.0 may through some errors

Make S3 Bucket in the AWS Console.
 
zappa init

Give bucket name as present on S3 or Create else it will be created as zappa-XXXXX

Edit zappa_setting.json and give "aws_region" : "Same as S3 Bucket Region"; If s3_bucket : "zappa-XXXXX" 
then you can mention any region of your choice

zappa deploy

After successful deployment, you will have some URL like XXXXXXX.execute-api.ap-south-1.amazonaws.com/<stage_name>

Copy and Paste "XXXXXX.execute-api.ap-south-1.amazonaws.com" in settings.py

zappa update <stage_name>

Visit your deploy on "XXXXXXX.execute-api.ap-south-1.amazonaws.com/<stage_name>"