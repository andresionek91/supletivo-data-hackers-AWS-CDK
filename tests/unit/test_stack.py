import pytest


@pytest.mark.parametrize(
    "type,count",
    [
        ("AWS::S3::Bucket", 0),
    ],
)
def test_resource_count(type, count, template_fixture):
    template_fixture.resource_count_is(type=type, count=count)


# def test_bucket(template_fixture):
#     template_fixture.has_resource_properties(
#         type="AWS::S3::Bucket",
#         props={
#             "BucketEncryption": {
#                 "ServerSideEncryptionConfiguration": [{"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]
#             },
#             "BucketName": "util-development-static-site-docs",
#             "LoggingConfiguration": {
#                 "DestinationBucketName": "util-development-access-logs",
#                 "LogFilePrefix": "S3Logs/util-development-static-site-docs/",
#             },
#             "OwnershipControls": {"Rules": [{"ObjectOwnership": "BucketOwnerEnforced"}]},
#             "PublicAccessBlockConfiguration": {
#                 "BlockPublicAcls": True,
#                 "BlockPublicPolicy": True,
#                 "IgnorePublicAcls": True,
#                 "RestrictPublicBuckets": True,
#             },
#             "VersioningConfiguration": {"Status": "Enabled"},
#         },
#     )
