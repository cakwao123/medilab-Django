from django.contrib import admin
from medilabapp.models import Product, Student, Company, Patient, Appointment

# Register your models here.
admin.site.register(Product)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Patient)
admin.site.register(Appointment)