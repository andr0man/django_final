from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
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