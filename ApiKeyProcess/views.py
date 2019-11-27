from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ApiKeyModel
from .serializer import ApiKeySerializer


@api_view(['GET'])
def index(request):
    return Response(
        {"message": "Welcome to LOGCam"},
        status=status.HTTP_201_CREATED
    )


@api_view(['GET', 'POST'])
def get_new_api_key(request):
    # get all the api keys
    if request.method == 'GET':
        api_key_data = ApiKeyModel.objects.filter(is_active=True).all()
        api_key_serializer = ApiKeySerializer(api_key_data, many=True)
        return Response({
            'success': True,
            'data': api_key_serializer.data
        },
            status=status.HTTP_201_CREATED)

    # generate api key and return it
    elif request.method == 'POST':
        api_key_serializer = ApiKeySerializer(data={})
        if api_key_serializer.is_valid():
            api_key_serializer.save()
            return Response({
                'success': True,
                'message': 'Api key generated successfully',
                'api_key': api_key_serializer.data
            },
                status=status.HTTP_201_CREATED)
        return Response(api_key_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
