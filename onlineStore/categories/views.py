from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories_list.html', { 'categories': categories } )

def category_page(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'categories/category_page.html', { 'category': category })

@login_required(login_url="/users/login")
def category_new(request):
    if request.method == "POST":
        form = forms.CreateCategory(request.POST, request.FILES)
        if form.is_valid():
            newCategory = form.save(commit=False)
            newCategory.user = request.user
            newCategory.save()
            return redirect("categories:list")
    else:
        form = forms.CreateCategory()
    return render(request, 'categories/category_new.html', { 'form': form })

@login_required(login_url="/users/login")
def category_delete(request, id):
    if request.user.is_authenticated:
        category = get_object_or_404(Category, id=id)
        category.delete()
    return redirect("categories:list")

@login_required(login_url="/users/login")
def category_edit(request, id):
    category = get_object_or_404(Category, id=id)

    if request.user.is_authenticated:
        if request.method == "POST":
            category.name = request.POST.get("name")
            category.save()
            return redirect("categories:list")

    return redirect("categories:list")