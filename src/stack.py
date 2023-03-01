import aws_cdk as cdk

from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3 as s3
from constructs import Construct
from typing_extensions import TypedDict
from typing_extensions import Unpack

from src.config import Config
from src.config import EnvironmentConfig


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
            id="DemoApiSupletivoDataHackersBucket",
            bucket_name=self.config.bucket_name,
            removal_policy=cdk.RemovalPolicy.DESTROY,  # somente por causa da demo
            auto_delete_objects=True,  # somente por causa da demo
        )

        _lambda.Function(
            scope=self,
            id="DemoApiSupletivoDataHackersLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset(self.config.code),
            timeout=cdk.Duration.seconds(self.config.timeout_seconds),
            memory_size=128,
            environment={
                "BUCKET_NAME": bucket.bucket_name,
            },
        )

        for idx in range(3):
            s3.Bucket(
                scope=self,
                id=f"ForLoopBucket{idx}",
                bucket_name=f"for-loop-bucket-data-hackers-{idx}",
                removal_policy=cdk.RemovalPolicy.DESTROY,  # somente por causa da demo
                auto_delete_objects=True,  # somente por causa da demo
            )

        # Add tags to everything in this stack
        cdk.Tags.of(self).add(key="owner", value="backend")
        cdk.Tags.of(self).add(key="type", value="service")
        cdk.Tags.of(self).add(key="name", value="DemoApiSupletivoDataHackers")
        cdk.Tags.of(self).add(key="stack", value=self.stack_name)
        cdk.Tags.of(self).add(key="stage", value=self.stage)
