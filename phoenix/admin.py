from django.contrib import admin

from .models import Rule, Trigger, Action

admin.site.register(Rule)
admin.site.register(Trigger)
admin.site.register(Action)