from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from market.models import Item
from market.forms import ItemForm
from django.utils import timezone
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User


def item_list_view(request):
    item_list = Item.objects.all().order_by('-published_date')
    paginator = Paginator(item_list, 3)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'market/item_list.html', {'items': items, 'request': request})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    user = str(item.author.username)
    return render(request, 'market/item_detail.html', {'item':item, 'user':user})


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
            item.author = request.user
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
            return redirect('item_list_view')
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
                return redirect('item_list_view')
        else:
            form = AuthenticationForm()
        return render(request, 'market/login.html', {'login_form': form})
    else:
        return redirect('item_list_view')


def logout_view(request):
    logout(request)
    return redirect('item_list_view')

def account_view(request):
    user = request.user
    item_list = Item.objects.filter(author=user)
    return render(request, 'market/account_view.html', {'item_list': item_list})

def profile_view(request, uname):
    user = get_object_or_404(User, username=uname)
    item_list = Item.objects.filter(author=user)
    return render(request, 'market/profile.html', {'item_list': item_list, 'user':user})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.author == request.user:
        if request.method == "POST":
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                post = form.save(commit=False)
                item.item_name = request.POST.get('item_name')
                item.department = request.POST.get('department')
                item.text = request.POST.get('text')
                item.price = request.POST.get('price')
                item.email = request.POST.get('email')
                item.published_date = timezone.now()
                post.save()
                return redirect('item_detail', pk=item.pk)
        else:
            form = ItemForm(instance=item)
            return render(request, 'market/item_edit.html', {'form': form})
    else:
        return render(request, 'market/item_detail.html', {'item':item, 'user':user})
