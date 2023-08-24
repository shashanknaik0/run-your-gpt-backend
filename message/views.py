from django.http import JsonResponse
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