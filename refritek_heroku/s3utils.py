from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


class S3StaticStorage(S3BotoStorage):
    """S3 storage backend that sets the static bucket."""
    def __init__(self, *args, **kwargs):
        super(S3StaticStorage, self).__init__(
            bucket=settings.AWS_STORAGE_BUCKET_NAME,
            *args, **kwargs
        )


StaticRootS3BotoStorage = lambda: S3StaticStorage(location='static')
MediaRootS3BotoStorage = lambda: S3BotoStorage(location='media')
