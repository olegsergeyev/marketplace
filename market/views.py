from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm, RegForm, AuthForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def item_list(request):
    items = Item.objects.all().order_by('published_date')
    print(request.user.is_authenticated)
    return render(request, 'market/item_list.html', {'items':items, 'request':request})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'market/item_detail.html', {'item':item})

@login_required(redirect_field_name='add_item', login_url='auth')
def add_item(request):
    #if not request.user.is_authenticated:
    #    return redirect('auth/')
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
    return render(request, 'market/add_item.html', {'form':form})

def registration(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = RegForm()
    return render(request, 'market/registration.html', {'reg_form':form})

def auth(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            print('kfjen')
            print(form.get_user())
            if user is not None:
                if user.is_active():
                    #login(request, user)
                    return redirect('item_list')
                #else:
                    #return redirect('market/accfail.html')
            #else:
                #return redirect('market/logfail.html')
        else:
            print(form.errors)
    else:
        form = AuthForm()
    return render(request, 'market/auth.html', {'auth_form':form})

def logout(request):
    logout(request)
