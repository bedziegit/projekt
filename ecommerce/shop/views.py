
from django.http import HttpResponse
import datetime
from .models import Product, Order, OrderProducts
from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic import ListView
from .forms import ProductForm

def welcome_view(request):
    return render(request,
                  "shop/base.html")
                 

def product_list(request):

    products = Product.objects.all()

    return render(request,
                  "shop/product/list.html",
                  {'products': products,
                   'show_navbar': False,})



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  
    return render(request, 'shop/product/product_form.html', {'product': product,
                                                              'show_navbar': False,})





def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)  # Przekierowanie po zapisaniu
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/product/product_form.html', {'form': form,
                                                              'show_navbar': False,})



def order_products_list(request, order_id):
    # Pobierz zamówienie na podstawie numeru zamówienia
    order = get_object_or_404(Order, number=order_id)
    
    # Pobierz wszystkie produkty powiązane z danym zamówieniem
    order_products = OrderProducts.objects.filter(order=order)
    
    return render(request, 'shop/product/order_products_list.html', {
        'order': order,
        'order_products': order_products,
        'show_navbar': False,
    })



def order_list(request):
    # Pobierz wszystkie zamówienia
    orders = Order.objects.all()
    
    return render(request, 'shop/order_list.html', {
        'orders': orders,
        'show_navbar': False,
    })