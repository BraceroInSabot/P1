from django.contrib import admin
from .models import Save

# Register your models here.
class SaveAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'total_amount', 'total_saved']
    search_fields = ['name']
    list_filter = ['created_at']
    list_per_page = 10

admin.site.register(Save, SaveAdmin)