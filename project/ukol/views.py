from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.views import View

# Create your views here.

def homework(request):
    return render(request,"homework.html")

def show_message(request):
    message = request.GET.get('message')
    return HttpResponse(f"<h1>{message}</h1>")

def choose_category(request):
    category = request.GET.get("category")  
    return render(request, "category_form.html", {"category": category})

def feedback_view(request):
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        print(f"Zpětná vazba od {name}: {message}")  
        success = True

    return render(request, "feedback_form.html", {"success": success})

class StaticPageView(TemplateView):
    template_name = "static_page.html"
    
class ContactView(View):
    def get(self, request):
        return render(request, "contact_form.html")

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print(f"Zpráva od {name} ({email}): {message}") 
        
        return render(request, "contact_form.html", {"success": True})
    
