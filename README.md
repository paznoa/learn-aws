# learn-aws  
## install docker desktop  
run DnamoDB container  
```
docker run amazon/dynamodb-local:latest -p 8000:8000
```
[Deploying DynamoDB locally on your computer](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)
## instsll aws CLI  
```
C:\Users\noapa>aws dynamodb list-tables --endpoint-url http://localhost:8000

You must specify a region. You can also configure your region by running "aws configure".  
C:\Users\noapa>aws configure  
AWS Access Key ID [None]: 1  
AWS Secret Access Key [None]: 2  
Default region name [eu-west-1]:  
Default output format [None]:  

C:\Users\noapa>aws dynamodb list-tables --endpoint-url http://localhost:8000  
```
