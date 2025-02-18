from django.shortcuts import render

def get_form(request):
    return render(request, "get_form.html")

def submit_form(request):
    data = request.GET.get("name", "unknown")
    return render(request, "submit_data.html", {"data": data})


def post_form(request):
    if request.method == "POST":
        data = request.POST["name"]
        return render(request, "submit_data.html", {"data": data})

    return render(request, "post_form.html")

def task(request):
    return render(request, "task.html")

def task_submit(request):
    data = request.GET.get("name", "unknown")
    print(data)
    return render(request, "task_submit.html", {"data": data})

def task2_submit(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        print(name,email,password)
        return render(request, "task2_submit.html", {"name": name, "email": email ,"password":password})
    return render(request, "task.html")