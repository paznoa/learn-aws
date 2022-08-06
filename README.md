# learn-aws  
## install docker desktop  
run DnamoDB container  
```
docker run amazon/dynamodb-local:latest  
```
[Deploying DynamoDB locally on your computer](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)
## instsll aws CLI  
C:\Users\noapa>aws dynamodb list-tables --endpoint-url http://localhost:8000

You must specify a region. You can also configure your region by running "aws configure".

C:\Users\noapa>aws configure
AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [None]: eu-west-1
Default output format [None]:
