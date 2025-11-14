from django.urls import path
from . import views

urlpatterns = [

    # main
    path("", views.index, name="main"),
    # --- Покупці ---
    path("customers/", views.customers_list, name="customers"),
    path("customers/add/", views.customer_add, name="customer_add"),
    path("customers/<int:pk>/", views.customer_detail, name="customer_detail"),

    # --- Продавці ---
    path("sellers/", views.sellers_list, name="sellers"),
    path("sellers/add/", views.seller_add, name="seller_add"),
    path("sellers/<int:pk>/", views.seller_detail, name="seller_detail"),

    # --- Товари ---
    path("products/", views.products_list, name="products"),
    path("products/add/", views.product_add, name="product_add"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),

    # --- Продажи ---
    path("sales/", views.sales_list, name="sales"),
    path("sales/add/", views.sale_add, name="sale_add"),
    path("sales/<int:pk>/", views.sale_detail, name="sale_detail"),

]
