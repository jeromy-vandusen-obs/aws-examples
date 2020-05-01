import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.client("dynamodb")
some_table = dynamodb.Table("some_table")

def get_item(key):
    dbresponse = some_table.get_item(Key={"someKey": {"S": key}})
    return dbresponse["Item"]

def get_items(value):
    dbresponse = some_table.query(KeyConditionExpression=Key("someKey").eq(value))
    return dbresponse["Items"]

def put_item(item):
    some_table.put_item({
        "key": {"S": item["key"]},
        "name": {"S": item["name"]},
        "code": {"S": item["code"]}
    })

def update_item(key, newValue):
    some_table.update_item(
        Key={"someKey": {"S": key}},
        UpdateExpression="SET some_value = :newValue",
        ExpressionAttributeValues={"newValue": {"S": newValue}}
    )

def delete_item(key):
    some_table.delete_item(Key={"someKey": {"S": key}})

def lambda_handler(event, context):
    item_count = len(get_items("test"))
    return "Found %d items." %(item_count)
