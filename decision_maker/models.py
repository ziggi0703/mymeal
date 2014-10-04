from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    link_to_menu = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return unicode(self.name)