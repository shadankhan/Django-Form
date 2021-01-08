from django.urls import path
from test1_app import views

urlpatterns = [
    path('about/', views.about_us, name="about_us"),
    path('contact/', views.contact_us, name="contact_us"),
]
