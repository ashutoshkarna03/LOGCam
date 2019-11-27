from rest_framework import serializers
from .models import ApiKeyModel


class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKeyModel
        # fields = '__all__'
        fields = (
            'api_key',
        )
