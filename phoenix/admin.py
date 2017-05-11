from django.contrib import admin

from .models import Signal, Rule, Trigger, Action

admin.site.register(Signal)
admin.site.register(Rule)
admin.site.register(Trigger)
admin.site.register(Action)