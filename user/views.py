import json
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def Signup(req):
    if req.method== "POST":
        data = json.loads(req.body)
        fname = data["fname"]
        lname = data["lname"]
        uname = data["uname"]
        pwd = data["pwd"]
        email = data["email"]
        
        myuser = User(username=uname,email=email,password=pwd)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        return HttpResponse("signin success")
    else:
        return HttpResponse("signin failed", status=505)
