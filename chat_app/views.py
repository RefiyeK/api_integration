from django.http import JsonResponse
from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
import json 
from .models import Chat

# Create your views here.
@csrf_exempt #dekaratör ile CSRF korumasını devre dışı bırakıyoruz, bu sayede POST istekleri çalışır

def chat_view(request):
    if request.method == "GET":
        chats = Chat.objects.all() #Tüm Chat'leri çek
        
        data = [
            {
                "id": chat.id, 
                "name": chat.name, 
                "message": chat.message, 
                "created_at": chat.created_at,
            } 
            for chat in chats
            ] #Her Chat'i dict'e çevirip listeye ekle 
        return JsonResponse(data, safe=False) #JsonResponse'ta liste dönerken safe=False olmali
      

    elif request.method == "POST":
        data = json.loads(request.body) #JSON'u parse et - POST isteğinden gelen verileri JSON formatında al 
        new_chat = Chat.objects.create(
            name=data["name"], 
            message=data["message"]
        ) #POST isteğinden gelen verilerle yeni Chat oluştur

        return JsonResponse({
            "id": new_chat.id, 
            "name": new_chat.name, 
            "message": new_chat.message, 
            "created_at": new_chat.created_at
            },
            ) #Oluşturulan Chat'i JSON formatında döndür
    
def chat_list_view(request):
    chats = Chat.objects.all()    # 1. tüm Chat'leri çek
    context = {'chats': chats}    # 2. template'e gönder
    return render(request, 'chat_app/chat.html', context)   # 3. template yolu