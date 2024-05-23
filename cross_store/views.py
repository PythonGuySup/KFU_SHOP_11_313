from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models.Customer import Customer
from .middleware.auth import login_requested
from .models import Products
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def shop(request):
    return render(request, "shop.html")


def blog(request):
    return render(request, "blog.html")


@login_requested
def private_office(request):
    customer = Customer.get_customer_by_id(request.session.get("customer"))
    context = {"first_name": customer.first_name, "last_name": customer.last_name}
    print(context)
    return render(request, template_name="private-office.html",
                  context=context)


def register(request):
    if request.method == "POST":
        data = request.POST
        if not Customer.get_customer_by_email(data["email"]):
            if data["password1"] == data["password2"]:
                country = "" if data["country"] == "Выбор страны" else data["country"]
                Customer().create_customer(email=data["email"], password=make_password(data["password1"]),
                                           first_name=data["first_name"], last_name=data["last_name"],
                                           country=country, locality=data["locality"],
                                           street_and_house=data["street_and_house"],
                                           index=data["index"], phone=data["phone"])
                return HttpResponse("<h3>Успешная регистрация!</h3>")
        else:
            return HttpResponse("<h3>Пользователь с таким email уже есть</h3>")
        print("Регистрация", data)
    else:
        return redirect("index")


def login(request):
    if request.method == "POST":
        data = request.POST
        password = data["password"]
        try:
            customer = Customer.get_customer_by_email(data["email"])
        except ValueError as e:
            return HttpResponse("<h3>Такого пользователя не существует</h3>")
        if customer:
            if check_password(password, customer.password):
                request.session["customer"] = customer.id
        print("Вход", data)
        return redirect("index")
    else:
        return redirect("index")


def logout(request):
    request.session.clear()
    return redirect('login')


def shop(request, page=1):
    page = int(page)
    product_quantity_at_page = 11
    product_quantity = Products.objects.all().count()
    products = Products.objects.filter(id__range=(product_quantity_at_page * (page - 1) + 1, product_quantity_at_page * page))
    products_hat = []
    products_catalog = []

    for i in range(0, len(products)):
        if products[i].name not in ["Месть", "Sigma"]:
            products_catalog.append(products[i])
            print("***", products[i].name)

    products_hat.append(Products.objects.get(name="Месть"))
    products_hat.append(Products.objects.get(name="Sigma"))

    return render(request, 'shop.html',
                  {'all_products': products, 'number_of_sublist': range(1, (product_quantity // 9) + 1),
                   'product_hat': products_hat, 'products_catalog': products_catalog, 'current_page': page})
