from django.urls import path
from .views import *


app_name = 'register'
urlpatterns = [
    path('agreement/', AgreementList.as_view(), name='Agreement')
]