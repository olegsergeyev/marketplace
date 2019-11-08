from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from market.models import Item
from market.forms import ItemForm
from django.utils import timezone
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required


def item_list(request):
    items = Item.objects.all().order_by('published_date')
    print(request.user.is_authenticated)
    return render(request, 'market/item_list.html', {'items': items, 'request': request})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'market/item_detail.html', {'item':item})


@login_required(redirect_field_name='add_item', login_url='login')
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
    return render(request, 'market/add_item.html', {'form': form})


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = UserCreationForm()
    return render(request, 'market/registration.html', {'reg_form': form})


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('item_list')
        else:
            form = AuthenticationForm()
        return render(request, 'market/login.html', {'login_form': form})
    else:
        return redirect('item_list')


def logout_view(request):
    logout(request)
    return redirect('item_list')
