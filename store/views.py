from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Category

import random


def home(request):
    # Get all best-selling products
    best_selling_products = list(Product.objects.filter(is_best_selling=True))

    # Shuffle to randomize
    random.shuffle(best_selling_products)

    # Take first 4 for trending, next 4 for best-selling (non-overlapping)
    trending = best_selling_products[:4]
    best_selling = best_selling_products[4:8] if len(best_selling_products) > 4 else best_selling_products[:4]

    return render(request, "index.html", {
        "trending": trending,
        "best_selling": best_selling
    })


def maintainance(request):
    return render(request, "maintainance_page.html")


# SHOP PAGE: All products, random order, 10 per page
def shop(request):
    products_list = list(Product.objects.all())  # convert queryset to list for shuffle
    random.shuffle(products_list)  # randomize order

    paginator = Paginator(products_list, 10)  # 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "shop.html", {
        "page_obj": page_obj,
        "num_of_products": len(products_list)
    })


# CATEGORY PAGES: Filtered products, 7 per page
def category_view(request, category_name, template_name, display_name):
    products_list = Product.objects.filter(category__name__icontains=category_name)
    paginator = Paginator(products_list, 7)  # 7 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, template_name, {
        "page_obj": page_obj,
        "category": display_name
    })


def haircare(request):
    return category_view(request, "haircare", "haircare.html", "Hair Care")


def makeup(request):
    return category_view(request, "makeup", "makeup.html", "Makeup")


def skincare(request):
    return category_view(request, "skincare", "skincare.html", "Skincare")

def contact(request):
    return render(request, "contact.html")