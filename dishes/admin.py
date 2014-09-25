from django.contrib import admin

from .models import Dish, Cuisine, MealType


admin.site.register(Cuisine)
admin.site.register(Dish)
admin.site.register(MealType)

