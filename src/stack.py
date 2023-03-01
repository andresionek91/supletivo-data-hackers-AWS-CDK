import aws_cdk as cdk

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

        s3.Bucket(
            scope=self,
            id="DemoApiSupletivoDataHackersBucket",
            bucket_name=self.config.bucket_name,
            removal_policy=cdk.RemovalPolicy.DESTROY,  # somente por causa da demo
            auto_delete_objects=True,  # somente por causa da demo
        )

        # Add tags to everything in this stack
        cdk.Tags.of(self).add(key="owner", value="backend")
        cdk.Tags.of(self).add(key="type", value="service")
        cdk.Tags.of(self).add(key="name", value="DemoApiSupletivoDataHackers")
        cdk.Tags.of(self).add(key="stack", value=self.stack_name)
        cdk.Tags.of(self).add(key="stage", value=self.stage)
