from django.urls import path

from . import views
from .views import *


urlpatterns = [
    # path('', views.Index)
    path('', StudentCreation.as_view())
]