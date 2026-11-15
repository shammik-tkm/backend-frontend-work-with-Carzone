
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .models import GalleryCategory, GalleryItem
from .forms import GalleryItemForm


# Main pages
def index(request):
    gallery_items = GalleryItem.objects.filter(is_active=True)
    return render(request, 'landing/index.html', {
        'gallery_items': gallery_items
    })


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
    categories = GalleryCategory.objects.all()

    return render(request, 'landing/admin/dashboard.html', {
        'items': items,
        'categories': categories
    })


@login_required(login_url='admin_login')
def custom_admin_add(request):
    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('custom_admin_dashboard')
    else:
        form = GalleryItemForm()

    return render(request, 'landing/admin/form.html', {
        'form': form,
        'title': 'Arbeit hinzufügen'
    })


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

    return render(request, 'landing/admin/form.html', {
        'form': form,
        'title': 'Arbeit bearbeiten'
    })


@login_required(login_url='admin_login')
def custom_admin_delete(request, pk):
    item = get_object_or_404(GalleryItem, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('custom_admin_dashboard')

    return render(request, 'landing/admin/delete_confirm.html', {
        'item': item
    })


# Category Management
@login_required(login_url='admin_login')
def custom_admin_categories(request):
    categories = GalleryCategory.objects.all().order_by('name')

    return render(request, 'landing/admin/categories.html', {
        'categories': categories
    })


@login_required(login_url='admin_login')
def custom_admin_category_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        slug = request.POST.get('slug', '').strip()

        if name:
            if not slug:
                slug = slugify(name)

            if GalleryCategory.objects.filter(slug=slug).exists():
                error = 'Diese URL-Kennung existiert bereits.'
                return render(request, 'landing/admin/category_form.html', {
                    'title': 'Kategorie hinzufügen',
                    'error': error,
                    'name': name,
                    'slug': slug
                })

            GalleryCategory.objects.create(name=name, slug=slug)
            return redirect('custom_admin_categories')

        return render(request, 'landing/admin/category_form.html', {
            'title': 'Kategorie hinzufügen',
            'error': 'Bitte gib einen Kategorienamen ein.',
            'name': name,
            'slug': slug
        })

    return render(request, 'landing/admin/category_form.html', {
        'title': 'Kategorie hinzufügen'
    })


@login_required(login_url='admin_login')
def custom_admin_category_edit(request, pk):
    category = get_object_or_404(GalleryCategory, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        slug = request.POST.get('slug', '').strip()

        if name:
            if not slug:
                slug = slugify(name)

            duplicate = GalleryCategory.objects.filter(
                slug=slug
            ).exclude(pk=category.pk).exists()

            if duplicate:
                return render(request, 'landing/admin/category_form.html', {
                    'title': 'Kategorie bearbeiten',
                    'category': category,
                    'name': name,
                    'slug': slug,
                    'error': 'Diese URL-Kennung wird bereits verwendet.'
                })

            category.name = name
            category.slug = slug
            category.save()

            return redirect('custom_admin_categories')

        return render(request, 'landing/admin/category_form.html', {
            'title': 'Kategorie bearbeiten',
            'category': category,
            'name': name,
            'slug': slug,
            'error': 'Bitte gib einen Kategorienamen ein.'
        })

    return render(request, 'landing/admin/category_form.html', {
        'title': 'Kategorie bearbeiten',
        'category': category,
        'name': category.name,
        'slug': category.slug
    })


@login_required(login_url='admin_login')
def custom_admin_category_delete(request, pk):
    category = get_object_or_404(GalleryCategory, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('custom_admin_categories')

    return render(request, 'landing/admin/category_delete_confirm.html', {
        'category': category
    })


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
            error = 'Falscher Benutzername oder Passwort'

    return render(request, 'landing/admin/login.html', {
        'error': error
    })


def admin_logout(request):
    logout(request)
    return redirect('admin_login')
