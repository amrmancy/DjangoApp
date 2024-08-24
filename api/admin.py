from django.contrib import admin
from .models import Order, MyUser


class MyUserAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ("id", "username", "email", "name", "address")

    # Fields to search by in the admin search bar
    search_fields = ("id", "username", "email", "name")

    # Filters for the right sidebar
    list_filter = ("id", "email", "name")

    # Fields that should be read-only in the admin interface
    readonly_fields = ("id",)


# Register the model with the admin site
admin.site.register(MyUser, MyUserAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "item_name", "amount", "created_at")
    search_fields = ("item_name",)
    list_filter = ("created_at", "user")
    readonly_fields = ("id", "created_at")


admin.site.register(Order, OrderAdmin)
