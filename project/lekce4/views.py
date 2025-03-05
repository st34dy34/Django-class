from django.shortcuts import render
from django.http import HttpResponse



def create_cookie(request):
    cookie = request.COOKIES.get("mode", "unknown")
    if cookie == "dark":
        new_cookie = "light"
    response = HttpResponse("Nastavenie cookie")
    response.set_cookie("mode", new_cookie, max_age=3600)  # expiracia 1 hodina
    return response


def get_cookie(request):
    cookie = request.COOKIES.get("mode", "unknown")
    return HttpResponse(f"Mode: {cookie}")


def delete_cookie(request):
    response = HttpResponse("Mazanie cookie")
    response.delete_cookie("mode")
    return response