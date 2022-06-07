from django.db import models


class Services(models.Model):
    service_name = models.CharField('Service', max_length=50)
    preview_serv = models.CharField('Preview', max_length=2000)
    full_text_serv = models.TextField('Description', max_length=10000)
    image_serv = models.ImageField(upload_to='services/static/services/img')

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

