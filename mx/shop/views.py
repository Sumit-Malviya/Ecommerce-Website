from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil
# Create your views here.


def index(request):
    # products = Product.objects.all()

    allProds = []
    catprods = Product.objects.values('category', 'id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        print(cat)
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = ceil(n / 4)
        allProds.append([prod, range(1, nslides), nslides])

    # allProds = [[products, range(1, nslides), nslides], [products, range(1, nslides), nslides]]
    params = {'allProds': allProds}
    # params = {'no_of_slides': nslides, 'range': range(1, nslides), 'product': products}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return HttpResponse("We are at search")


def productView(request, myid):
    # Fetch the product using id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    return HttpResponse("We are at checkout")

