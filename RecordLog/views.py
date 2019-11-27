from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LogsModel
from .serializer import LogsSerializer


@api_view(['GET'])
def index(request):
    return Response(
        {"message": "Welcome to LOGCam"},
        status=status.HTTP_201_CREATED
    )


@api_view(['POST'])
def record_logs(request):
    # inserting in logs
    logs_serializer = LogsSerializer(data=request.data)
    if logs_serializer.is_valid():
        logs_serializer.save()
        return Response({
            'success': True,
            'message': 'Log inserted successfully',
            'data_inserted': logs_serializer.data
        },
            status=status.HTTP_201_CREATED)
    return Response(logs_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_logs(request):
    api_key = request.data['api_key']
    log_data = LogsModel.objects.filter(api_key=api_key).all()
    print(log_data)
    print(type(log_data))
    serializer = LogsSerializer(log_data, many=True)
    return Response({
        'success': True,
        'data': serializer.data
    },
        status=status.HTTP_201_CREATED)

