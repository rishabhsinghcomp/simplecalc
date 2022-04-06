from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="Home"),
    path('demo/',views.ij),
    path('demo/addition/',views.add,name="adder")
]