from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/products/', views.order_products_list, name='order_products_list'),
]
