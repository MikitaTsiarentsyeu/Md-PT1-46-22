from django.db import models





class Review(models.Model):
    person_name = models.CharField(max_length=50, blank=False)
    mail = models.EmailField(blank=False)
    content = models.TextField(blank=False)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.person_name



class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50, blank=False)
    ingridients = models.TextField(blank=False)
    recipe = models.TextField(blank=False)
    image = models.ImageField(upload_to='uploads')

    def __str__(self) -> str:
        return self.recipe_name
    





    

