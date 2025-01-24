from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view),
    path('products', views.product_list),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
]