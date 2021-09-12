from django.contrib import admin
from .models import BillingModel


# Register your models here.


@admin.register(BillingModel)
class BillingAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'item', 'quantity', 'price', 'date', 'time']
