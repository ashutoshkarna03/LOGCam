from .models import ApiKeyModel


def validate_api_key_if_exists(api_key):
    is_api_key_valid = ApiKeyModel.objects.filter(api_key=api_key).exists()
    return is_api_key_valid
