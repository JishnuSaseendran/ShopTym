from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Item
from .forms import ItemForm, UserForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views.generic import View

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def item_list(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'ecapp/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'ecapp/item_detail.html', {'item': item})

def register(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return render(request, 'ecapp/item_list.html', {'items': items})

    else:
        form = UserForm()
    return render(request, 'ecapp/register.html', {'form': form})        


@login_required
def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.item_logo = request.FILES['item_logo']
            file_type = item.item_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'item': item,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'ecapp/item_edit.html', context)
            item.published_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'ecapp/item_edit.html', {'form': form})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.item_logo = request.FILES['item_logo']
            file_type = item.item_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'item': item,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'ecapp/item_edit.html', context)
            item.published_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'ecapp/item_edit.html', {'form': form})

@login_required
def item_draft_list(request):
    items = Item.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'ecapp/item_draft_list.html', {'items': items})

@login_required
def item_publish(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.publish()
    return redirect('item_detail', pk=pk)

@login_required
def item_remove(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('item_list')
