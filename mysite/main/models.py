from django.db import models
from datetime import datetime
#from datetime import date

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.tutorial_title

class Orders(models.Model):
    po_number = models.CharField(max_length=20)
    purchase_date = models.DateField()
    confirmed_date = models.DateField(default='', blank=True, null=True)
    planned_delivery_date = models.DateField(default=None, blank=True, null=True)
    shipped_date = models.DateField(default=None, blank=True, null=True)
    delivered_to_novastar_date = models.DateField(default=None, blank=True, null=True)
    item_status = models.CharField(max_length=50)
    item = models.TextField()
    order_quantity = models.IntegerField()
    open_items = models.TextField()
    op_item_quantity = models.IntegerField()
    shipped_items = models.TextField()
    sh_quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.item
