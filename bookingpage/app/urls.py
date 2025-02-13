from django.urls import path
from app import views


urlpatterns=[
    # path('home',views.home),
    path('',views.d_home),
    path('booking',views.d_booking),
    path('appoinment',views.d_appoinment),
    path('home',views.home),
    path('card',views.d_card),
    

]