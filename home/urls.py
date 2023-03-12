from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "K P.PHARMA"
admin.site.site_title = "K P.PHARMA admin portal"
admin.site.index_title = "Welcome to K P.Pharma"

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about , name='about'),
    path("services", views.services , name='services'),
    path("contact", views.contact , name='contact'),
    
    
]
 