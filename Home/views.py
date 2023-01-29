from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def home(request):
    
    match request.method:
        case "POST":
            user = {
                "name":request.POST.get("username","Anonim User"),
                "age":20
            }
            return JsonResponse(data=user)
        case "GET":
            return render(request,"index.html")
        # case _:
        #     pass

    # if request.method == "POST":
    #     pass 
    # if request.method == "GET":
    #     pass