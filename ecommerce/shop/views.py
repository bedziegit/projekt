
from django.http import HttpResponse
import datetime
from .models import Product
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
                  {'products': products})



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  
    return render(request, 'product_detail.html', {'product': product})





def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)  # Przekierowanie po zapisaniu
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/product/product_form.html', {'form': form})
