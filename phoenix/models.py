from django.db import models


class Signal(models.Model):
    name = models.CharField(max_length=50)

class Rule(models.Model):
    services = models.TextField(max_length=200)
    attributes = models.TextField(max_length=300)

class Trigger(models.Model):
    signal_id = models.ForeignKey(Signal, on_delete=models.CASCADE)
    rules = models.CharField(max_length=50)
    threshold_level = models.CharField(max_length=50)