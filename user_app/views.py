from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse, JsonResponse


# http://127.0.0.1:8000/user/message

def greet(request):
    return HttpResponse("Hii, Good Morning")


def get_name(request):
    return HttpResponse("my name is madhavi")


def details(request):
    return HttpResponse([{
"name": "amit",
"email":"amit@gmail.com",
"address":"hyd"
},
{
"name": "hanu",
"email":"hanu@gmail.com",
"address":"hyd",
}])