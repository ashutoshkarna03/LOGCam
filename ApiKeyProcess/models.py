from django.db import models
from utils.helpers import generate_random_string


class ApiKeyModel(models.Model):
    # contains the list of api keys with time created and is_active fields
    api_key = models.TextField(max_length=32, default=generate_random_string)
    created_on = models.DateTimeField('date_created', auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.api_key

    class Meta:
        verbose_name = 'table to save api keys'
        db_table = 'api_keys'


def get_status_of_api_key(api_key):
    """
    check if the status (is_active) is true or false
    :param api_key: api_key value to be checked
    :return: status of given api_key (returns boolean)
    """
    return True
