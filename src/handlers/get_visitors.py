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

  return {
    "statusCode": 200,
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    },
    "body": json.dumps({
      "visitors": str(res["Item"]['VisitorCount'])
    }),
  }
