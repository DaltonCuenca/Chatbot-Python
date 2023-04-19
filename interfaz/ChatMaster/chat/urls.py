from django.urls import path
from .views import chatView

urlpatterns = [
    path('', chatView, name='chat'),
]