from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserAdmin(UserAdmin):
     model = User
     fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Avatar de l'utilisateur",
            {
                'fields': (
                    'avatar',
                )            }
        )
    )




admin.site.register(User,UserAdmin)