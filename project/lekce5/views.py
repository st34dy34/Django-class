from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

@login_required
def add_perm(request):
    user = request.user
    permission = Permission.objects.get(codename='can_publish')
    user.user_permissions.add(permission)
    user.save()

    return redirect("lek5_view")

@permission_required('lek5.can_publish', raise_exception=True)
def restricted_view(request):
    return HttpResponse("Len pre používateľov s oprávnením 'view_model'.")