from rest_framework import serializers
from .models import LogsModel


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogsModel
        # fields = '__all__'
        fields = (
            'api_key',
            'log_message',
            'log_properties',
            'optional_args_key',
            'optional_args_value',
            'recorded_on'
        )


