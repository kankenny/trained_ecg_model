import json
import base64
from lambda_endpoint import predict
from util.util import delimiter_decor, ECGData


@delimiter_decor
def lambda_handler(event, context):
    try:
        if event.get('isBase64Encoded'):
            body = json.loads(base64.b64decode(event['body']))
        else:
            body = json.loads(event['body'])
        
        payload = ECGData.parse_obj(body)
        res = predict(payload)
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Prediction successful",
                "result": res
            })
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "An error occurred",
                "error": str(e)
            })
        }
