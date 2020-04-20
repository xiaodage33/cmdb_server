from django.shortcuts import render
from django.http import  HttpResponse
from api import  *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import  json

@csrf_exempt
def index(request):
    # print(request.GET)
    print(request.POST)
    print(request.body)
    content=request.body.decode('utf-8')
    server_info_dict = json.loads(content)
    print(server_info_dict)

    # return render(request,'show.html',{'host':host,'info':info})



    return HttpResponse("haha")



def show_server(request):

    return render (request,'show.html')