"""LOGCam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RecordLog.views import index, record_logs, get_logs
from ApiKeyProcess.views import get_new_api_key, update_api_key_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('record-logs', record_logs, name='record the logs'),
    path('get-logs', get_logs, name='get the logs'),
    path('get-api-key', get_new_api_key, name='get the new api key'),
    path('update-api-key-status', update_api_key_status, name='update the is_active status of apikey'),
]
