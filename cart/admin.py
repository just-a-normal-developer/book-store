from django.contrib import admin

# Register your models here.
from cart.models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
    )
    raw_id_fields = [
        "user",
        "added_books",
    ]


admin.site.register(Cart, CartAdmin)
