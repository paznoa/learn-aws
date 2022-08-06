# learn-aws  
## install docker desktop  
run DnamoDB container  
```
docker run amazon/dynamodb-local:latest -p 8000:8000
```
[Deploying DynamoDB locally on your computer](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)  

## install NoSQL workbench
go to operation builder and define new local connection  
click on the local connections and keep the credentials (access key, secret key)  

## install aws CLI  
```
C:\Users\noapa>aws dynamodb list-tables --endpoint-url http://localhost:8000
You must specify a region. You can also configure your region by running "aws configure".  
C:\Users\noapa>aws configure  
AWS Access Key ID [None]: <access key from step above>  
AWS Secret Access Key [None]: <secret key from step above>  
Default region name []: localhost  
Default output format [None]:  
```
[DynamoDB local usage notes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.UsageNotes.html)  

```
aws dynamodb list-tables --endpoint-url http://localhost:8000 
aws dynamodb create-table --table-name MyTableName  --attribute-definitions '[{"AttributeName":"id", "AttributeType":"S"}, {"AttributeName":"createdAt", "AttributeType":"S"}]'  --key-schema '[{"AttributeName":"id", "KeyType":"HASH"}, {"AttributeName":"createdAt", "KeyType":"RANGE"}]'  --provisioned-throughput '{"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}'  --endpoint-url http://localhost:8000
aws dynamodb scan --table-name MyTableName --endpoint-url http://localhost:8000
aws dynamodb describe-table  --table-name MyTableName  --endpoint-url http://localhost:8000
```


## Python example 
https://github.com/aws-samples/aws-dynamodb-examples/tree/master/DynamoDB-SDK-Examples/python/WorkingWithItems
