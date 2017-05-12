from django.contrib import admin

from .models import Signal, Trigger, Action

admin.site.register(Signal)
admin.site.register(Trigger)
admin.site.register(Action)