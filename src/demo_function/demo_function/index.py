import json
import os

import boto3

from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from mypy_boto3_s3 import S3Client


tracer = Tracer()
logger = Logger()
app = APIGatewayRestResolver()

BUCKET_NAME = os.environ["BUCKET_NAME"]


@app.get("/files")
@tracer.capture_method
def list_files_from_s3() -> dict:
    """List files from S3 bucket"""

    logger.info("Listing files from S3 bucket")

    s3_client: S3Client = boto3.client("s3")
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)

    logger.debug(f"S3 Response: {response}")

    return {"files": [content.get("Key") for content in response.get("Contents", [])]}


@app.get("/file")
@tracer.capture_method
def get_file_from_s3() -> dict:
    """Get file from S3 bucket"""

    logger.info("Getting file from S3 bucket")

    file_name: str = app.current_event.get_query_string_value(name="file_name", default_value="")  # type: ignore
    logger.debug(f"File name: {file_name}")

    s3_client: S3Client = boto3.client("s3")
    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)

    logger.debug(f"S3 Response: {response}")

    return {"file_name": file_name, "content": response.get("Body").read().decode("utf-8")}


@app.put("/file")
@tracer.capture_method
def upload_file_to_s3() -> dict:
    """Upload file to S3 bucket"""
    logger.info("Uploading file to S3 bucket")

    body = json.loads(app.current_event.body)  # type: ignore
    logger.debug(f"Body: {body}")

    file_name = body.get("file_name")
    content = body.get("content")

    s3_client: S3Client = boto3.client("s3")
    response = s3_client.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=content)

    logger.debug(f"S3 Response: {response}")

    return {"file": file_name}


# You can continue to use other utilities just as before
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    """Lambda handler"""
    return app.resolve(event, context)
