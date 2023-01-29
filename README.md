# DjangoAjax
Django-da AJAX istifadəsi


&copy;  Shukurov Mushvig


| Sosial Hesablarım |
|-------------------|
|[Youtube](https://www.youtube.com/@mushvigsh)|
|[Instagram](https://www.instagram.com/mushvigsh)|


# A-Z izah

> `Video IZAH` : (https://youtu.be/ecYBYenVedk)

1. `python -m venv myvenv` ilə venv yükləyirik
2. "CTRL + SHIFT + P" kombinasiyası ilə menyunu açıb Python Select İnterpreter yazırıq
3. Enter İnterpreter Path + Browse your file... + myvenv/Scripts/python.exe seçirik
4. `pip install Django` ilə Django-nu yükləyirik
5. `python manage.py startapp Home` ilə Home adlı app yaradırıq
6. Core/settings.py INSTALLED_APPS[..., 'Home.apps.HomeConfig',] 
7. 'templates' folderi yaradıb, Core/settings.py Templates ["DIRS":"templates"] yazırıq
8. Home/views.py faylında :
<pre>
from django.shortcuts import render
from django.http import JsonResponse
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
</pre>

9. Core/urls.py 
<pre>
from django.contrib import admin
from django.urls import path
from Home.views import home
# localhost:8000
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
]
</pre>


10. Templates/index.html faylı yaradırıq
11. index.html faylında :
<pre>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>

    <form method="POST" id="bizimform">
        {% csrf_token %}
        <input type="text" name="username" required>
        <button type="submit">Klikle</button>
    </form>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.6.3.min.js" integrity="sha256-pvPw+upLPUjgMXY0G+8O0xUf+/Im1MZjXxxgOcBQBXU=" crossorigin="anonymous"></script>

    <script>
        $bizimform = $("#bizimform")
        $bizimform.submit(function(e){
            e.preventDefault()
            $serializedData = $(this).serialize()
            $.post("{% url 'home' %}",$serializedData,function(response){
                console.log("User Name :" + response.name)
                console.log("User age :" + response.age)
                $bizimform.trigger("reset")
            })
        })
    </script>
</body>
</html>
</pre> 