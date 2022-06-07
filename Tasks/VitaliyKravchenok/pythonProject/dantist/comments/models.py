from django.db import models


class Comments(models.Model):
    author = models.CharField('Name', max_length=30, default='anonymous')
    date = models.DateTimeField('Publication date')
    review_text = models.TextField('Comment', max_length=10000)
    author_email = models.EmailField(blank=False, default='example@email.com')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
