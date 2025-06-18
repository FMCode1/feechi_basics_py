from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inventory

# Create your views here.
def home_view(request):
    return render(request, 'crud.html')

def inventory_action(request):
    if request.method == 'POST':
        entered_product_name = request.POST.get('product_name')
        entered_product_price = request.POST.get('product_price')
        selected_action = request.POST.get('crud_action')

        if selected_action == "create":
            # Model_name.objects.create(property='value', property='value')
            Inventory.objects.create(product_name=entered_product_name, product_price=entered_product_price)

        elif selected_action == "read":
            # Model_Name.objects.all()
            Inventory.objects.all()[0].values(product_name = entered_product_name)

        elif selected_action == "update":
            # entry= Model_Name.objects.all()[4]
            # entry.target_property = ‘updated value’
            # entry.save()
            updated_entry = Inventory.objects.all()[product_name, product_price]
            updated_entry.product_name = entered_product_name
            updated_entry.product_price = entered_product_price
            updated_entry.save()

        elif selected_action == "delete":
            # entry= Model_Name.objects.all()[4]
            # entry.delete()
            deleted_entry = Inventory.objects.all()[product_name, product_price]
            deleted_entry.delete()
    
    return HttpResponse("Invalid request.")
