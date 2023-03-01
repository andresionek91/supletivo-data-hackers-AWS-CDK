import aws_cdk as cdk

from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_s3 as s3
from constructs import Construct
from src.config import Config
from src.config import EnvironmentConfig
from typing_extensions import TypedDict
from typing_extensions import Unpack


class Params(TypedDict):
    """Parameters for the stack"""

    stage: str
    env: cdk.Environment


class DemoApi(cdk.Stack):
    """Demo API with Lambda function"""

    def __init__(self, scope: Construct, id: str, **kwargs: Unpack[Params]) -> None:
        description = "Demo API with Lambda function"
        super().__init__(scope, id, description=description, env=kwargs.get("env"))

        self.stage = kwargs.get("stage")
        self.config: Config = getattr(EnvironmentConfig(), self.stage)

        bucket = s3.Bucket(
            scope=self,
            id="DemoApiSupletivoDataHackers",
            bucket_name=f"spdh-{self.stage}-demo-api",
            removal_policy=cdk.RemovalPolicy.DESTROY,  # Delete bucket when stack is deleted
            auto_delete_objects=True,  # Delete all objects in the bucket when the bucket is deleted
        )

        handler = lambda_.DockerImageFunction(
            scope=self,
            id="DemoApiSupletivoDataHackersHandler",
            description="Demo API with Lambda function",
            code=lambda_.DockerImageCode.from_image_asset(
                directory=self.config.code,
            ),
            timeout=cdk.Duration.seconds(amount=self.config.timeout_seconds),
            memory_size=self.config.memory_size_mb,
            ephemeral_storage_size=cdk.Size.mebibytes(amount=self.config.ephemeral_storage_size_mb),
            log_retention=self.config.log_retention,
            dead_letter_queue_enabled=self.config.dead_letter_queue_enabled,
            environment={
                "LOG_LEVEL": self.config.log_level,
                "BUCKET_NAME": bucket.bucket_name,
                **self.config.extra_environment,
            },
        )

        bucket.grant_read_write(handler)

        api = apigw.RestApi(
            scope=self,
            id="DemoApiSupletivoDataHackersApi",
            rest_api_name="DemoApiSupletivoDataHackers",
            description="Demo API with Lambda function",
        )

        demo_api_integration = apigw.LambdaIntegration(handler=handler)

        files_resource = api.root.add_resource("files")
        files_resource.add_method("GET", demo_api_integration, api_key_required=False)
        file_resource = api.root.add_resource("file")
        file_resource.add_method("GET", demo_api_integration, api_key_required=False)
        file_resource.add_method("PUT", demo_api_integration, api_key_required=False)

        # Add tags to everything in this stack
        cdk.Tags.of(self).add(key="owner", value="backend")
        cdk.Tags.of(self).add(key="type", value="service")
        cdk.Tags.of(self).add(key="name", value="DemoApiSupletivoDataHackers")
        cdk.Tags.of(self).add(key="stack", value=self.stack_name)
        cdk.Tags.of(self).add(key="stage", value=self.stage)
