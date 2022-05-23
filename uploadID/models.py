from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class Id_item(models.Model):
    ID_num = models.CharField(max_length=100)
    Location_found = models.CharField(default="", max_length=100)
    Image = models.ImageField(upload_to='images')
    Find_Date = models.DateTimeField(auto_now_add=True)
    Pick_up_location = models.CharField(max_length=100)

    def __str__(self):
        return self.ID_num
    