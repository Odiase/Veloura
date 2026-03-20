from django.urls import path
from .views import *

urlpatterns = [

    path("", home, name="home"),
    path("products/", products_coming_soon, name="products_coming_soon"),
    path("maintainance/", maintainance, name="maintainance"),
    path("shop/", shop, name="shop"),
    path("makeup/", makeup, name="makeup"),
    path("skincare/", skincare, name="skincare"),
    path("haircare/", haircare, name="haircare"),
    path("contact/", contact, name="contact"),

]