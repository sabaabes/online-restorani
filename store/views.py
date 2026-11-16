from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Product
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def menu_view(request):
    categories = Category.objects.all()  
    context = {
        'items': categories  
    }
    return render(request, 'store/menu.html', context)

def category_products(request, category_id):
    category = Category.objects.get(id=category_id)  
    products = Product.objects.filter(category=category)  
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'store/category_products.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')  
    else:
        form = UserCreationForm()
    
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('menu')

def add_to_cart(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    
    cart = request.session.get('cart', {})
    str_product_id = str(product_id)
    
    if str_product_id in cart:
        cart[str_product_id] += quantity
    else:
        cart[str_product_id] = quantity
        
    request.session['cart'] = cart
    
   
    return redirect(request.META.get('HTTP_REFERER', 'menu'))

def cart_view(request):
    cart = request.session.get('cart', {})
    products_in_cart = []
    total_price = 0
    
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=int(product_id))
        total_price += product.price * quantity
        products_in_cart.append({'product': product, 'quantity': quantity})
        
    context = {
        'cart_items': products_in_cart,
        'total_price': total_price
    }
    return render(request, 'store/cart.html', context)

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('cart_view')

def checkout(request):
    cart = request.session.get('cart', {})
    total_price = 0
    
    
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=int(product_id))
        total_price += product.price * quantity

    if request.method == 'POST':
        
        if 'cart' in request.session:
            del request.session['cart']
        return render(request, 'store/checkout_success.html')

    context = {
        'total': total_price,
    }
    return render(request, 'store/checkout.html', context)