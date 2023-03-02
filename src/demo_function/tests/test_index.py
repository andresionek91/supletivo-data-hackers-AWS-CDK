import os

from unittest import mock

import boto3

from moto import mock_s3


MOCK_BUCKET_NAME = "foo-bar"


with mock.patch.dict(os.environ, {"BUCKET_NAME": MOCK_BUCKET_NAME}):
    from demo_function.index import list_files_from_s3


MOCK_BUCKET_NAME = "foo-bar"


@mock_s3
def test_list_files_from_s3() -> None:
    """Test list_files_from_s3"""

    with mock_s3():
        s3_client = boto3.client("s3")
        s3_client.create_bucket(Bucket=MOCK_BUCKET_NAME)
        s3_client.put_object(Bucket=MOCK_BUCKET_NAME, Key="file1.txt")
        s3_client.put_object(Bucket=MOCK_BUCKET_NAME, Key="file2.txt")

        actual = list_files_from_s3()
        expected = {"files": ["file1.txt", "file2.txt"]}

        assert actual == expected
