from django.db import models
import datetime
from datetime import timezone

from django_unixdatetimefield import UnixDateTimeField


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def epoch(self):
        date_create = self.created_at
        date_example = str(date_create)
        date_format = datetime.datetime.strptime(
            date_example, '%Y-%m-%d %H:%M:%S.%f%z')
        unix_time = datetime.datetime.timestamp(date_format)
        return int(round(unix_time))*1000
