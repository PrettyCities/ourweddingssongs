import os

import boto3

from ows_settings import AWS_BUCKET
from ows_settings import AWS_DYNAMO_REGION
from ows_settings import AWS_DYNAMO_TABLE
from ows_settings import WEBSITE_DIRECTORY


class AwsServices:
    dynamodb = boto3.resource("dynamodb", region_name=AWS_DYNAMO_REGION)
    table = dynamodb.Table(AWS_DYNAMO_TABLE)

    @classmethod
    def add(cls, **kwargs):
        kwargs_with_value = {k: v for k, v in kwargs.items() if v is not None}
        cls.table.put_item(Item=kwargs_with_value)

    @classmethod
    def get_items(cls):
        response = cls.table.scan()
        return response['Items']

    @classmethod
    def upload_website(cls, full_load=False):
        s3 = boto3.client('s3')

        local_directory = WEBSITE_DIRECTORY
        bucket = AWS_BUCKET
        destination = ""

        # enumerate local files recursively
        for root, dirs, files in os.walk(local_directory):

            for filename in files:

                if filename != "index.html":
                    if not full_load:
                        continue

                extra_args = {'ContentType': "text/html", 'ACL': "public-read"}

                # construct the full local path
                local_path = os.path.join(root, filename)

                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, local_directory)
                s3_path = os.path.join(destination, relative_path)
                print("Uploading {} to s3".format(relative_path))
                s3.upload_file(local_path, bucket, s3_path, ExtraArgs=extra_args)


if __name__ == "__main__":
    AwsServices.upload_website(full_load=True)
