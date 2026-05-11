from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Category

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_detail.html', {'category': category, 'products': products})


@login_required # Cette ligne force l'utilisateur à être connecté pour voir son panier
def cart(request):
    cart = request.session.get("cart", {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total = Decimal("0.00")

    for product in products:
        quantity = cart.get(str(product.id), 0)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    return render(request, "products/cart.html", {
        "cart_items": cart_items,
        "total": total,
    })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        cart = request.session.get("cart", {})
        product_id_key = str(product.id)
        cart[product_id_key] = cart.get(product_id_key, 0) + 1
        request.session["cart"] = cart
        request.session.modified = True
        messages.success(request, f"{product.name} a été ajouté au panier.")
        return redirect("cart")

    return redirect("product_detail", product_id=product.id)


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        cart = request.session.get("cart", {})
        cart.pop(str(product.id), None)
        request.session["cart"] = cart
        request.session.modified = True
        messages.success(request, f"{product.name} a été retiré du panier.")

    return redirect("cart")

