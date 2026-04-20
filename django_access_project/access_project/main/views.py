from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Item

@login_required
def home(request):
    user = request.user
    group = user.groups.first()

    if group:
        items = Item.objects.filter(allowed_group=group.name)
    else:
        items = []

    return render(request, 'home.html', {'items': items})