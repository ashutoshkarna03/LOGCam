from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ApiKeyModel
from .serializer import ApiKeySerializer
from .validation import validate_api_key_if_exists


@api_view(['GET'])
def index(request):
    return Response(
        {"message": "Welcome to LOGCam"},
        status=status.HTTP_201_CREATED
    )


@api_view(['GET', 'PUT'])
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
    elif request.method == 'PUT':
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


@api_view(['POST'])
def update_api_key_status(request):
    api_key_to_update = request.data['api_key']
    new_status_value = request.data['new_status']

    # validate if new_status_value is Boolean or not
    if type(new_status_value) is not bool:
        return Response({
            "success": False,
            "message": "new_status should be Boolean type"
        }, status=status.HTTP_400_BAD_REQUEST)

    # validate api_key provided in request
    if not validate_api_key_if_exists(api_key_to_update):
        return Response({
            "success": False,
            "message": "api_key is not valid or does not exist"
        }, status=status.HTTP_400_BAD_REQUEST)

    # update the status (is_active) with the new value
    ApiKeyModel.objects.filter(api_key=api_key_to_update).update(is_active=new_status_value)
    return Response({
        "success": True,
        "message": "status updated"
    }, status=status.HTTP_201_CREATED)
