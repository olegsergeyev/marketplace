from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm, RegForm
from django.utils import timezone

import hashlib

def item_list(request):
    items = Item.objects.all().order_by('published_date')
    return render(request, 'market/item_list.html', {'items':items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'market/item_detail.html', {'item':item})

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.item_name = request.POST.get('item_name')
            item.department = request.POST.get('department')
            item.text = request.POST.get('text')
            item.price = request.POST.get('price')
            item.email = request.POST.get('email')
            item.published_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'market/add_item.html', {'add_form':form})

def registration(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            user_r = form.save(commit=False)
            user_r.username = request.POST.get('username')
            user_r.name = request.POST.get('name')
            user_r.email = request.POST.get('email')
            user_r.password = hashlib.md5(request.POST.get('password').encode('utf-8')).hexdigest()
            user_r.save()
            return redirect('item_list')
    else:
        form = RegForm()
    return render(request, 'market/registration.html', {'reg_form':form})
