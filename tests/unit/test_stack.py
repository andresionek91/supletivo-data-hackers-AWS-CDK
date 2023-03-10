import pytest


@pytest.mark.parametrize(
    "type,count",
    [
        ("AWS::S3::Bucket", 1),
    ],
)
def test_resource_count(type, count, template_fixture):
    template_fixture.resource_count_is(type=type, count=count)


def test_bucket(template_fixture):
    template_fixture.has_resource_properties(
        type="AWS::S3::Bucket",
        props={
            "BucketName": "spdh-development-demo-api",
        },
    )
