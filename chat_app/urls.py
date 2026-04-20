from django.urls import path
from .views import chat_view, chat_list_view #Aynı app'in views.py'ından chat_view fonksiyonunu al

urlpatterns = [
    path('', chat_view, name='chat'),
    path('view/', chat_list_view, name='chat_list'),
]

#chat_view = Bu URL'e eşleşen istekleri chat_view'e yönlendir