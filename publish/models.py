from django.db import models

class Ride(models.Model):
    # fields of the model
    source = models.TextField()
    destination = models.TextField()

    class Meta:
        app_label = 'PackTravel.publish'

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
