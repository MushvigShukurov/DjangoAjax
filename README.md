# DjangoAjax
Django-da AJAX istifadəsi


&copy;  Shukurov Mushvig


| Sosial Hesablarım |
|-------------------|
|[Youtube](https://www.youtube.com/@mushvigsh)|
|[Instagram](https://www.instagram.com/mushvigsh)|


# A-Z izah

1. `python -m venv myvenv` ilə venv yükləyirik
2. "CTRL + SHIFT + P" kombinasiyası ilə menyunu açıb Python Select İnterpreter yazırıq
3. Enter İnterpreter Path + Browse your file... + myvenv/Scripts/python.exe seçirik
4. `pip install Django` ilə Django-nu yükləyirik
5. `python manage.py startapp Home` ilə Home adlı app yaradırıq
6. Core/settings.py INSTALLED_APPS[..., 'Home.apps.HomeConfig',] 
7. 'templates' folderi yaradıb, Core/settings.py Templates ["DIRS":"templates"] yazırıq
8. Home/views.py faylında :
`
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
`