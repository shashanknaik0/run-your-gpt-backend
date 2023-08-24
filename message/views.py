import json
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Message

# Create your views here.
@login_required
def message(request):
    if request.method == "GET":
        userId = request.user.id
        items = Message.objects.all().filter(user_id = userId).order_by('created_at')
        result = []
        for x in items:
            result.append({"id":x.id,"user_input":x.user_input,"response":x.response, "created_at":x.created_at})

        return JsonResponse(result,safe=False)
    
    elif request.method == "POST":
        data = json.loads(request.body)
        user = request.user
        user_input = data["user_input"]
        response = data["response"]
        newMessage = Message(user_id = user ,user_input=user_input,response=response)
        newMessage.save()
        return HttpResponse("saved cart")