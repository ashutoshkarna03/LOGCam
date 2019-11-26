from rest_framework import serializers
from .models import LogsModel, ApiKeyModel


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


class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKeyModel
        # fields = '__all__'
        fields = (
            'api_key',
        )

