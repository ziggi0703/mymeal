from django.contrib import admin
from decision_maker.models import Restaurant


# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    fields = ['name', 'link_to_menu']

admin.site.register(Restaurant, RestaurantAdmin)