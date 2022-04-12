from django.db import models

# Create your models here.


class Tourist(models.Model):

    TRAVEL_TYPE = [('a', 'All tours'), ('d', 'Day tours'), ('g', 'Guided tours'), ('r', 'Road trips'), ('s', 'Special offer')]
    TRAVEL_SERVICES = [('c', 'Car rental'), ('a', 'Accommodation'), ('f', 'Flights')]
    MAILING_LIST = [('y', 'Yes'), ('n', 'No')]

    title = models.CharField(max_length=10,blank=False, default="Travel request")
    name = models.CharField(blank=False, max_length=50)
    email = models.EmailField(blank=False)
    phone = models.CharField(blank=False, max_length=20)
    convenient_time_to_call = models.CharField(blank=False, max_length=100)
    travel_type = models.CharField(max_length=1,blank=False, choices=TRAVEL_TYPE)
    travel_services = models.CharField(max_length=1,blank=True, choices=TRAVEL_SERVICES)
    activities = models.TextField(blank=True, max_length=150)
    attractions = models.TextField(blank=True, max_length=150)
    attractions = models.TextField(blank=True, max_length=150)
    comments = models.TextField(blank=True, max_length=150)
    sign_up_for_our_mailing_list = models.CharField(max_length=1,blank=False, choices=MAILING_LIST)
    issued = models.DateTimeField()

    def __str__(self) -> str:
        return self.title



