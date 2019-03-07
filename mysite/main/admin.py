from django.contrib import admin
from .models import Tutorial
from .models import Orders
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
#class OrderStatusAdmin(admin.ModelAdmin):
#    fieldsets = [("PO")]

class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
    ("Content", {"fields": ["tutorial_content"]})]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Tutorial, TutorialAdmin)

class OrdersAdmin(admin.ModelAdmin):
    fields = ["po_number",
              "purchase_date",
              "confirmed_date",
              "planned_delivery_date",
              "shipped_date",
              "delivered_to_novastar_date",
              "item_status",
              "item",
              "order_quantity",
              "open_items",
              "op_item_quantity",
              "shipped_items",
              "sh_quantity",
              "price"]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Orders, OrdersAdmin)
