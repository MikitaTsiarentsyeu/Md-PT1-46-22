from django.db import models

# Create your models here.
class Feedback(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.full_name


class CallBack(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.name