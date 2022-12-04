from django.urls import path
from . import views

app_name = "FAQ"

urlpatterns = [
    path('', views.homepage, name = 'homepage'),

    path('quessions', views.quessions, name = 'quessions'),
    path('contact', views.contact, name = 'contact'),
    path('company', views.company, name = 'company'),

]