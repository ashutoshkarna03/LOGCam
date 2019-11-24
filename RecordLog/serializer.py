from rest_framework import serializers
from .models import Logs


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#
# class TimelineSerializer(serializers.Serializer):
#     tweets = BookSerializer(many=True)
#     articles = AuthorSerializer(many=True)
#     fields = '__all__'
