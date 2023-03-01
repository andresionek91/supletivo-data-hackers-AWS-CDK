import json
import os


BUCKET_NAME = os.environ["BUCKET_NAME"]


def lambda_handler(event: dict, context: dict) -> dict:
    """Lambda handler"""
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Hello from Lambda!",
                "bucket_name": BUCKET_NAME,
            }
        ),
    }
