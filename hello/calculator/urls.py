from django.urls import path
from . import views

urlpatterns=[
    path('',views.intro,name='introcalc'),
    path('calcresult/',views.operation,name='processing')
]
