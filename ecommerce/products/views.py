from django.shortcuts import render, get_list_or_404
from .models import Product, Category


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
def product_detail(request, product_id):
    product = get_list_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_list_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    
    return render(request, 'products/category_detail.html', {'category': category, 'products': products})
