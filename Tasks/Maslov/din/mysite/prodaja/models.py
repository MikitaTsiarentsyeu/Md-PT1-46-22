from email.mime import image
from unittest.util import _MAX_LENGTH
from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length= 120)
    post = models.TextField()
    date= models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title
class Product(models.Model):
  

  name_product = models.CharField('название товара', max_length=50)

  def __str__(self):
    return self.name_product