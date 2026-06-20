from django.urls import path
from . import views
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.func, name="index"),
    path('register/', views.func1, name="register"),
    path('login/', views.func2, name="login"),
    path('home/', views.func3, name="home"),
    path('profile/', views.func4, name="profile"),
    path('logout/', views.func5, name="logout"),
    path('view_users/', views.view_users, name='view_users'),    
    path('editprofile/', views.func7, name="editprofile"),
    path('delete_user/<int:id>/', views.func8, name="delete_user"),
    path('product/', views.func9, name="product"),
    path('display/', views.func10, name="display"),
    path('delete_product/<int:id>/', views.func11, name='delete_product'),
    path('editproduct/<int:product_id>/', views.func12, name='edit_product'),
    path('addtocart/<int:id>/', views.func13, name='addtocart'),
    path('displaycart/', views.func14, name='displaycart'),
    path('payment/', views.paynow, name='payment'),
    path('paynow/', views.func15, name='paynow'),
    path('stripe-checkout/', views.stripe_checkout, name='stripe_checkout'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('displayorder/', views.func16, name='displayorder'),
    path('orderitems/<int:id>/', views.func17, name="orderitems"),
    path('feedback/<int:id>/', views.func18, name="feedback"),
    path('viewfeedback/<int:id>/', views.func19, name="viewfeedback"), 
    path('viewallfeedbacks/',views.func20,name="viewallfeedbacks"),
    
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('admin_user_orders/<int:user_id>/', views.admin_user_orders, name='admin_user_orders'),
    path('add_product/', views.add_product, name='add_product'),
    path('seller_products/', views.seller_products, name='seller_products'),
    path('seller_orders/', views.seller_orders, name='seller_orders'),
    path('seller_returns/', views.seller_returns, name='seller_returns'),
    path('return_order_item/<int:item_id>/', views.return_order_item, name='return_order_item'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('checkout_all/', views.checkout_all, name='checkout_all'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('review/<int:product_id>/',views.add_review,name='add_review'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
        path(
        'wishlist/',
        views.wishlist_view,
        name='wishlist'
    ),

    path(
        'wishlist/add/<int:product_id>/',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),
    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),
]

urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    

