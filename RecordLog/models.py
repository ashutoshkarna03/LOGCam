from django.db import models
# from __future__ import unicode_literals
from django.contrib.postgres.fields import ArrayField, JSONField
from utils.helpers import generate_random_string


class Logs(models.Model):
    log_id = models.TextField(max_length=32, default=generate_random_string())
    api_key = models.TextField(max_length=32)
    log_message = models.TextField(max_length=2048)
    log_properties = JSONField(default=dict)
    optional_args_key = models.TextField(max_length=2048, default='')
    optional_args_value = models.TextField(max_length=2048, default='')
    is_deleted = models.BooleanField(default=False)
    recorded_on = models.DateTimeField('date_recorded', auto_now_add=True)

    def __str__(self):
        return "{} on {}".format(
            self.log_id,
            self.recorded_on.strftime('%Y-%m-%m'))

    class Meta:
        verbose_name = 'table to save logs with optional properties'
        db_table = 'logs'



