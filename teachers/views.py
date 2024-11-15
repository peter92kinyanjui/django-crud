from itertools import product

from django.shortcuts import render,redirect
from idna.idnadata import scripts
from nacl.hashlib import scrypt
from urllib3 import request
from teachers.models import Product, NewEntry


# Create your views here.
def home(request):
    return render(request,'index.html')

def insert(request):
    return render(request,'insert.html')

def insert_data(request):
    if request.method == 'POST':
        prod_name = request.POST['prod_name']
        prod_price = request.POST['prod_price']
        prod_category = request.POST['prod_category']
        prod_qty = request.POST['prod_qty']
        prod_desc = request.POST['prod_desc']
        prod_img = request.FILES['prod_img']

        product = Product(
                          prod_name=prod_name,
                          prod_price=prod_price,
                          prod_category=prod_category,
                          prod_qty=prod_qty,
                          prod_desc=prod_desc,
                          prod_img=prod_img
        )
        product.save()

        return redirect('/')

    return render(request,'insert.html')

def view_product(request):
    products = Product.objects.all()
    return render(request,'viewproducts.html',{'products':products})

#retrieving single item
def get_product(request,id):
    product=Product.objects.get(id=id)
    return render(request,'details.html',{'product':product})

#update an entry
def update_product(request,id):
    product=Product.objects.get(id=id)
    if request.method == 'POST':
        #getting the new values
        prod_name = request.POST['prod_name']
        prod_price = request.POST['prod_price']
        prod_category = request.POST['prod_category']
        prod_qty = request.POST['prod_qty']
        prod_desc = request.POST['prod_desc']
        prod_img = request.FILES['prod_img']

        #Reassigning the new values
        product.prod_name = prod_name
        product.prod_price = prod_price
        product.prod_category = prod_category
        product.prod_qty = prod_qty
        product.prod_desc = prod_desc
        product.prod_img = prod_img

        product.save()
        return redirect('/view_products/')

    return render(request,'update.html',{'product':product})

def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/view_products/')




def Studinsert(request):
    return render(request,'StudFom.html')




def NewStudInsert(request):
    if request.method == 'POST':
        stud_reg=request.POST['stud_reg']
        stud_name=request.POST['stud_name']
        stud_course= request.POST['stud_course']

        NewStudent = NewEntry (
            stud_reg=stud_reg,
            stud_name=stud_name,
            stud_course=stud_course
        )
        NewStudent.save()
        redirect('/viewstudents/')

    return render(request,'StudFom.html')

def viewstudents(request):
    return render(request,'viewstudents.html')

def Stud_Details(request):
    NewStudents = NewEntry.objects.all()
    return render(request,'stud_details.html',{'NewStudents':NewStudents})



