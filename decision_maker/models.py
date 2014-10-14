from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    link_to_menu = models.URLField(blank=True)
    food_type = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(null=True)
    todays_vote = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.name)