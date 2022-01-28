from django.contrib import admin
from inventory.models import *
# Register your models here.
@admin.register(laptop,desktop,mobile)
class ViewAdmin(admin.ModelAdmin):
    pass