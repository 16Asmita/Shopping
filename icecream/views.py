from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Icecream
from .models import Contact
from django.contrib import messages

def icecream(request):
    if request.method == "POST":
        ice_name = request.POST.get('search')
  
        icecreams = Icecream.objects.filter(name=ice_name)

    else:
        icecreams = Icecream.objects.all()
    return render(request, "icecream.html", {
        "icecreams": icecreams
    })

def icecream_1(request):
    template_name = "home.html"
    results = []
    if request.method == "POST":
        ice_name = request.POST.get('search')
        search_type = request.POST.get('search_type')

        #print(search_type)

        if search_type == "icecream":
            results = Icecream.objects.filter(name=ice_name)
            template_name = "icecream.html"

        else:
            results = Contact.objects.filter(name=ice_name)
            template_name = "contact.html"


    return render(request, template_name, {
        "results": results

    })


def details(request, ice_id):
    icecream = Icecream.objects.get(pk=ice_id)
    # select * from products where id=22
    return render(request, "details.html", {"icecream":icecream })


def remove(request, ice_id):
    icecream = Icecream.objects.get(pk=ice_id)
    # Delete  from products where id=22
    icecream.delete()
    messages.success(request, "Your record deleted successfully...")
    return redirect("/icecream/")

def product_create(request):
    return render(request, "insert.html")
 
def product_save(request):
    if request.method == "POST":
        product_name = request.POST.get('name')
        product_price = request.POST.get('price')
        
        product = Icecream(name=product_name, price=product_price)
        product.save()

        messages.success(request, 'Product has been created successfully.')
        return redirect('/icecream/')
    

def product_update(request, ice_id):
    icecream = Icecream.objects.get(pk=ice_id)
    return render(request, "update.html", {"icecream":icecream})

def product_edit(request, ice_id):
    if request.method == 'POST':        

        # Form data
        icecream_name = request.POST.get('name')        
        icecream_price = request.POST.get('price')

        # update product set name=Mouse, price=1234 where product_id=12

        # Update product.
        icecream = Icecream.objects.get(pk=ice_id)
        icecream.name = icecream_name
        icecream.price = icecream_price
        icecream.save()

        messages.success(request, 'Product has been updated successfully.')
        
    return redirect('/icecream/')
