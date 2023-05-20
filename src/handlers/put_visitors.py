import json
import boto3
from boto3.dynamodb.conditions import Key

DDB_TABLE_NAME = "cloud-resume-challenge"
DDB_CLIENT = boto3.client('dynamodb', region_name="us-east-1")
DDB_TABLE = boto3.resource('dynamodb', region_name="us-east-1")
TABLE = DDB_TABLE.Table(DDB_TABLE_NAME)

def lambda_handler(event, context):
  res = TABLE.get_item(
    Key = {
      "ID" : "VisitorCount"
    }
  )

  TABLE.update_item(
    Key={
      "ID" : "VisitorCount"
    },
    UpdateExpression="SET VisitorCount = :val1",
    ExpressionAttributeValues={
      ":val1" : res["Item"]['VisitorCount'] + 1
    }
  )
  return {
    "statusCode": 200,
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  }
