from django.contrib import admin
from .models import Name
# Register your models here.


class NameAdmin(admin.ModelAdmin):
    list_display = ('First', 'Last', 'YearDate', 'GraveKeeper')

admin.site.register(Name, NameAdmin)