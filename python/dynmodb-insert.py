from __future__ import print_function # Python 2/3 compatibility
import boto3, json, decimal
import time

from botocore.exceptions import ClientError


def insert_record(dynamodb,i_table_name,i_attribute_not_exist,i_item):
    table = dynamodb.Table(i_table_name)
    conditinalexpression = 'attribute_not_exists(%s)'%(i_attribute_not_exist)
    #Insert new user data into the system
    try:
        response = table.put_item(
        Item=i_item,
        ConditionExpression=conditinalexpression

        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return(e.response['Error']['Code'])

    print("PutItem succeeded:")
    print(json.dumps(response,indent=4))
    print (i_item)
    return 0


def main():
    dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000/')
    
    expDate = int(time.time())
    input_item = {"id": "b33332244442ar" , "createdAt": "2343","expDate":expDate }
   
    retval=insert_record(dynamodb,'MyTableName','id',input_item)
    print(retval)

if __name__ == '__main__':
    main()
