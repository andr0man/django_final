from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.products_list, name="list"),
    path('<int:id>', views.product_page, name="page"),
    path('new-product/', views.product_new, name="new-product"),
]