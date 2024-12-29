from django.shortcuts import render
from collections import defaultdict
from .models import Inventory, Category

def menu_page(request):
    categories = Category.objects.all().order_by('name')  # Fetch and order categories
    foods = Inventory.objects.all().order_by('category', 'name')  # Fetch and order foods

    # Group foods by category as a dictionary
    menu_data = {
        category: foods.filter(category=category) for category in categories
    }

    context = {
        'menu_data': menu_data
    }
    return render(request, 'index.html', context)