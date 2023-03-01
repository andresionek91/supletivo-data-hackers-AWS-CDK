from enum import Enum

import aws_cdk as cdk

from src.stack import DemoApi


class AWSAccount(Enum):
    """AWS Account IDs"""

    DEVELOPMENT = "267631547124"
    STAGING = "123456789012"
    PRODUCTION = "987654321098"


app = cdk.App()

DemoApi(
    scope=app,
    id="DemoApi-Development",
    env=cdk.Environment(
        account=AWSAccount.DEVELOPMENT.value,
        region="us-east-1",
    ),
    stage="development",
)

DemoApi(
    scope=app,
    id="DemoApi-Staging",
    env=cdk.Environment(
        account=AWSAccount.STAGING.value,
        region="us-east-1",
    ),
    stage="staging",
)

DemoApi(
    scope=app,
    id="DemoApi-Production",
    env=cdk.Environment(
        account=AWSAccount.PRODUCTION.value,
        region="us-east-1",
    ),
    stage="production",
)

app.synth()
