from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'parent'
    )
    list_editable = ('__all__')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Genre, MPTTModelAdmin)
