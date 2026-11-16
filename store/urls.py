from django.urls import path
from .views import menu_view, category_products, register_view, login_view, logout_view, cart_view, add_to_cart, clear_cart, checkout 


urlpatterns = [
    path('', menu_view, name='menu'),
    path('category/<int:category_id>/', category_products, name='category_products'), 
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
path('cart/', cart_view, name='cart_view'),
path('clear-cart/', clear_cart, name='clear_cart'),
path('checkout/', checkout, name='checkout'),
]