from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Customer, Seller, Product, Sale
from .forms import CustomerForm, SellerForm, ProductForm, SaleForm


# Main
def index(request):
    return render(request, "layout.html")

# Покупці 
def customers_list(request):
    customers = Customer.objects.all()

    context = {
        "title": "Покупатели",
        "items": customers,
        "columns": ["Имя", "Фамилия", "Телефон", "Email"],
        "fields": ["first_name", "last_name", "phone", "email"],
        "add_url": reverse("customer_add")
    }

    return render(request, "list.html", context)


def customer_add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customers")
    else:
        form = CustomerForm()

    return render(request, "form.html", {
        "form": form,
        "title": "Добавить покупателя",
        "back_url": reverse("customers")
    })


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    fields = [
        ("Имя", customer.first_name),
        ("Фамилия", customer.last_name),
        ("Телефон", customer.phone),
        ("Email", customer.email),
    ]

    return render(request, "detail.html", {
        "title": f"Покупатель: {customer}",
        "fields": fields,
        "back_url": reverse("customers")
    })

# Продавці 
def sellers_list(request):
    sellers = Seller.objects.all()

    context = {
        "title": "Продавцы",
        "items": sellers,
        "columns": ["Имя", "Фамилия", "Телефон", "Позиция"],
        "fields": ["first_name", "last_name", "phone", "position"],
        "add_url": reverse("seller_add")
    }

    return render(request, "list.html", context)


def seller_add(request):
    if request.method == "POST":
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sellers")
    else:
        form = SellerForm()

    return render(request, "form.html", {
        "form": form,
        "title": "Добавить продавца",
        "back_url": reverse("sellers")
    })


def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)

    fields = [
        ("Имя", seller.first_name),
        ("Фамилия", seller.last_name),
        ("Телефон", seller.phone),
        ("Email", seller.email),
        ("Дата приема", seller.hired_date),
        ("Позиция", seller.get_position_display()), #type: ignore
    ]

    return render(request, "detail.html", {
        "title": f"Продавец: {seller}",
        "fields": fields,
        "back_url": reverse("sellers")
    })


#  Товари
def products_list(request):
    products = Product.objects.all()

    context = {
        "title": "Товары",
        "items": products,
        "columns": ["Название", "Количество"],
        "fields": ["name", "quantity_in_stock"],
        "add_url": reverse("product_add")
    }

    return render(request, "list.html", context)


def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()

    return render(request, "form.html", {
        "form": form,
        "title": "Добавить товар",
        "back_url": reverse("products")
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    fields = [
        ("Название", product.name),
        ("Описание", product.description),
        ("Количество на складе", product.quantity_in_stock),
    ]

    return render(request, "detail.html", {
        "title": f"Товар: {product.name}",
        "fields": fields,
        "back_url": reverse("products")
    })



# Продажи
def sales_list(request):
    sales = Sale.objects.select_related("customer", "seller", "product")

    context = {
        "title": "Продажи",
        "items": sales,
        "columns": ["Покупатель", "Продавец", "Товар", "Сумма", "Дата"],
        "fields": ["customer", "seller", "product", "amount", "date"],
        "add_url": reverse("sale_add")
    }

    return render(request, "list.html", context)


def sale_add(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sales")
    else:
        form = SaleForm()

    return render(request, "form.html", {
        "form": form,
        "title": "Добавить продажу",
        "back_url": reverse("sales")
    })


def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)

    fields = [
        ("Покупатель", sale.customer),
        ("Продавец", sale.seller),
        ("Товар", sale.product),
        ("Дата продажи", sale.date),
        ("Сумма", sale.amount),
        ("Количество", sale.quantity),
    ]

    return render(request, "detail.html", {
        "title": f"Продажа #{pk}",
        "fields": fields,
        "back_url": reverse("sales")
    })



