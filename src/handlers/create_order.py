import json
import os
import boto3
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
orders_table = os.environ.get('ORDERS_TABLE')

def handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        product_id = body.get('product_id')
        quantity = body.get('quantity', 1)
        
        if not product_id:
            return {'statusCode': 400, 'body': json.dumps({'error': 'product_id required'})}

        order_id = str(uuid.uuid4())
        table = dynamodb.Table(orders_table)
        
        item = {
            'id': order_id,
            'product_id': product_id,
            'quantity': quantity,
            'status': 'PENDING'
        }
        
        table.put_item(Item=item)

        return {
            'statusCode': 201,
            'body': json.dumps(item),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
