from django.contrib import admin
from .models import Restaurant , Inclusive_type, Food_type

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
     model = Restaurant
     field = "__all__"
     
     
     
admin.site.register(Restaurant,RestaurantAdmin)


class Inclusive_typeAdmin(admin.ModelAdmin):
     model = Inclusive_type
     field = "__all__"
     
     
     
admin.site.register(Inclusive_type,Inclusive_typeAdmin)


class Food_typeAdmin(admin.ModelAdmin):
     model = Food_type
     field = "__all__"
     
     
     
admin.site.register(Food_type,Food_typeAdmin)