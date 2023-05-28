from django.contrib import admin
from.models import Books , Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user' , 'book' , 'text' , 'datetime_created', )

# Register your models here.
admin.site.register(Books)
admin.site.register(Comments , CommentsAdmin)

