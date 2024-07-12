
from django.contrib import admin
from django.urls import path
from medilabapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('start/', views.start,name='start'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),

    path('contact/', views.contact,name='contact'),
    path('Patient/', views.Patient,name='Patient'),
    path('appointment/', views.Appoint,name='Appoint'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete),
]
