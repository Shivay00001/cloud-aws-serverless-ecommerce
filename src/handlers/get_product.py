import json
import os
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('PRODUCTS_TABLE')

def handler(event, context):
    table = dynamodb.Table(table_name)
    
    # Mock data if table is empty
    if table.scan()['Count'] == 0:
        table.put_item(Item={'id': '1', 'name': 'Laptop', 'price': Decimal('999.99')})
        table.put_item(Item={'id': '2', 'name': 'Phone', 'price': Decimal('499.99')})

    response = table.scan()
    items = response.get('Items', [])
    
    # Convert Decimals to float for JSON serialization
    for item in items:
        for k, v in item.items():
            if isinstance(v, Decimal):
                item[k] = float(v)

    return {
        'statusCode': 200,
        'body': json.dumps({'products': items}),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
