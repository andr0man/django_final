from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', { 'products': products } )

def product_page(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_page.html', { 'product': product })

@login_required(login_url="/users/login")
def product_new(request):
    if request.method == "POST":
        form = forms.CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            newproduct = form.save(commit=False)
            newproduct.user = request.user
            newproduct.save()
            return redirect("products:list")
    else:
        form = forms.CreateProduct()
    return render(request, 'products/product_new.html', { 'form': form })