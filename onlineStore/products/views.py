from django.shortcuts import render, redirect, get_object_or_404
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

@login_required(login_url="/users/login")
def product_delete(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id)
        product.delete()
    return redirect("products:list")

@login_required(login_url="/users/login")
def product_edit(request, id):
    product = get_object_or_404(Product, id=id)

    if request.user.is_authenticated:
        if request.method == "POST":
            product.name = request.POST.get("name")
            product.description = request.POST.get("description")
            product.price = request.POST.get("price")

            if "image" in request.FILES:
                product.image = request.FILES["image"]

            product.save()
            return redirect("products:list")

    return redirect("products:list")
