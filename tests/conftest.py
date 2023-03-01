import aws_cdk as cdk
import pytest

from app import AWSAccount
from aws_cdk.assertions import Template

from src.stack import DemoApi


@pytest.fixture(scope="session")
def app_fixture():
    return cdk.App()


@pytest.fixture(scope="session")
def stack_fixture(app_fixture):
    return DemoApi(
        scope=app_fixture,
        id="TestDemoApi",
        env=cdk.Environment(account=AWSAccount.DEVELOPMENT.value, region="us-east-1"),
        stage="development",
    )


@pytest.fixture(scope="session")
def template_fixture(stack_fixture):
    return Template.from_stack(stack_fixture)
