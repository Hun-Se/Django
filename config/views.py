from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return render(request,"main.html")

def burger_list(request):
    return render(request,"burger_list.html")

def burger_search(request):
    keyword = request.GET.get("keyword")
    print(keyword)

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    
    else:
        burgers = Burger.objects.none()
    print(burgers)

    context = {
        "bugers": burgers,
    }

    return render(request, "burger_search.html", context)