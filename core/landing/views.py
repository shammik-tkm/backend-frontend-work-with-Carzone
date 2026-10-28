from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import GalleryCategory, GalleryItem
from .forms import GalleryItemForm

# Main pages
def index(request):
    gallery_items = GalleryItem.objects.filter(is_active=True)
    return render(request, 'landing/index.html', {'gallery_items': gallery_items})

def gallery(request):
    categories = GalleryCategory.objects.all()
    gallery_items = GalleryItem.objects.filter(is_active=True)
    return render(request, 'landing/gallery.html', {
        'categories': categories,
        'gallery_items': gallery_items
    })

# Custom Admin Panel
@login_required(login_url='admin_login')
def custom_admin_dashboard(request):
    items = GalleryItem.objects.all()
    return render(request, 'landing/admin/dashboard.html', {'items': items})

@login_required(login_url='admin_login')
def custom_admin_add(request):
    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_dashboard')
    else:
        form = GalleryItemForm()
    return render(request, 'landing/admin/form.html', {'form': form, 'title': 'Dobavit rabotu'})

@login_required(login_url='admin_login')
def custom_admin_edit(request, pk):
    item = get_object_or_404(GalleryItem, pk=pk)
    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_dashboard')
    else:
        form = GalleryItemForm(instance=item)
    return render(request, 'landing/admin/form.html', {'form': form, 'title': 'Redaktirovat rabotu'})

@login_required(login_url='admin_login')
def custom_admin_delete(request, pk):
    item = get_object_or_404(GalleryItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('custom_admin_dashboard')
    return render(request, 'landing/admin/delete_confirm.html', {'item': item})

# Login / Logout
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('custom_admin_dashboard')
    
    error = None
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('custom_admin_dashboard')
        else:
            error = 'Nepravilnyy login ili parol'
            
    return render(request, 'landing/admin/login.html', {'error': error})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')