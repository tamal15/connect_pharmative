from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    projucts = Products.objects.all()
    context = {
        'products': projucts
    }
    return render(request, "index.html",context)

def products(request):
    projucts=Products.objects.all()
    context={
        'products':projucts
    }
    return render(request, "shop.html",context)


def select_product(request,medicine_name):
    select_product=Products.objects.get(slug=medicine_name)

    return render(request,"shop-single.html",{'select_product':select_product})


def search(request):
    product=request.GET['query']
    select_product=Products.objects.get(name=product)

    return render(request, "shop-single.html",{'select_product':select_product})



def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def form_submission(request):
    #if request.method=="POST":

     c_fname=request.POST["c_fname"]
     c_lname=request.POST["c_lname"]
     c_email=request.POST["c_email"]
     c_subject=request.POST["c_subject"]
     c_message=request.POST["c_message"]
     form=Form.objects.create(c_fname=c_fname, c_lname=c_lname, c_email=c_email, c_subject=c_subject, c_message=c_message)
     form.save()
     return render(request, "contact.html")





