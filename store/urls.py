from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, ProductCreateView, ProductListView, CartView, Homepage,AddToCartView

urlpatterns = [
    path('', Homepage.as_view(), name='product_list'),
    path('product-list', ProductListView.as_view(), name='product_list'),
    
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),

  
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='product_list'), name='logout'),
    path('create-product/', ProductCreateView.as_view(), name='product_create'),
    
]



