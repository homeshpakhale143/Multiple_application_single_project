from django.urls import path
from cloth.views import *
app_name='something'

urlpatterns=[
    path('tracks/',tracks,name='tracks')

]