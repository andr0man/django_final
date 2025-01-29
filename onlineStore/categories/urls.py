from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    path('', views.categories_list, name="list"),
    path('<int:id>', views.category_page, name="page"),
    path('new-category/', views.category_new, name="new-category"),
]