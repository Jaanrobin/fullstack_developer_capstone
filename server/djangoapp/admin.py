from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # This defines how many empty model forms to display


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Including the CarModel inline


# CarModelAdmin class (optional if you want a separate admin for CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "year", "car_make", "dealer_id")


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
