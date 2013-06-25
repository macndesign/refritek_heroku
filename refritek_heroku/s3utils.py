from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


class S3StaticStorage(S3BotoStorage):
    def url(self, name):
        """
        Change URL's generated in the following format: http(s)://bucket.name.s3.amazonaws.com/.../
        Into the format: http(s)://s3.amazonaws.com/bucket.name/.../
        """
        url = super(S3StaticStorage, self).url(name)
        bucket_name = self.bucket.name
        if "%s.s3.amazonaws.com" % bucket_name in url:
            url = url.replace("%s.s3.amazonaws.com/" % bucket_name, "s3.amazonaws.com/%s/" % bucket_name)
        return url


StaticRootS3BotoStorage = lambda: S3StaticStorage(location='static')
MediaRootS3BotoStorage = lambda: S3BotoStorage(location='media')
