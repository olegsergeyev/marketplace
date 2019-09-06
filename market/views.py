from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
from django.utils import timezone

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
            rrr = request.body
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
