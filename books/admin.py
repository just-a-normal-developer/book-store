from django.contrib import admin
from .models import Books, Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "book",
        "text",
        "datetime_created",
        "is_active",
        "recommend",
    )


admin.site.register(Books)
admin.site.register(Comments, CommentsAdmin)
