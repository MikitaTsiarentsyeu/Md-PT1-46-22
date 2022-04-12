from django.contrib import admin
from .models import Review
from .models import Recipe



admin.site.register(Review)
admin.site.register(Recipe)