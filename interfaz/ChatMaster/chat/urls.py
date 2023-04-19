from django.urls import path
from .views import chatbot, borrar_conversacion

urlpatterns = [
    path('', chatbot, name='chat'),
    path('borrar-conversacion/', borrar_conversacion, name='borrar_conversacion'),
]