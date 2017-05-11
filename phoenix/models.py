from django.db import models


class Action(models.Model):
    name = models.CharField(max_length=50, default="None")
    key = models.CharField(max_length=50, default="None")
    def __str__(self):
        return self.name

class Signal(models.Model):
    name = models.CharField(max_length=50, default="None")
    def __str__(self):
        return self.name

class Rule(models.Model):
    name = models.CharField(max_length=50, default="None")
    services = models.TextField(max_length=200)
    attributes = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Trigger(models.Model):
    name = models.CharField(max_length=50, default="None")
    signal_id = models.ForeignKey(Signal, on_delete=models.CASCADE)
    rules = models.ManyToManyField(Rule)
    threshold_level = models.CharField(max_length=50)
    action_taken = models.ForeignKey(Action, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
