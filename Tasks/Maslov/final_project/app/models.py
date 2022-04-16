from django.db import models

class Post(models.Model):

    POST_TYPES = [('c', 'copyright'), ('p', 'public license'), ('m', 'marketing')]

    title = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    issued = models.DateTimeField()
    image = models.ImageField(upload_to='uploads')
    post_type = models.CharField(max_length=1, blank=False, choices=POST_TYPES)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Author(models.Model):

    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False, primary_key=True)

    def __str__(self) -> str:
        return self.name
