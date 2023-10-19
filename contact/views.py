from django.shortcuts import render
from .models import Contact

def contact(request):
    if request.method == "POST":
        contact_name = request.POST.get('search')
        contacts = Contact.objects.filter(name=contact_name)

    else:
        contacts = Contact.objects.all()
        
    return render(request, "contact.html", {
        "contacts": contacts
    })

def data(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    # select * from products where id=22
    return render(request, "data.html", {"contact":contact })

