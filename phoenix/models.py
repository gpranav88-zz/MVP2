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
    SERVICES_CHOICES = (
        ('identity','IDENTITY'),
        ('order', 'ORDER'),
    )
    ATTRIBUTES_CHOICES = (
        ('email','User Email'),
        ('cancelled_order', 'Cancelled Orders'),
        ('refund_order', 'Refund Orders'),
    )
    name = models.CharField(max_length=50, default="None")
    services = models.CharField(max_length=10, default='identity', choices=SERVICES_CHOICES)
    attributes = models.CharField(max_length=10, default='email', choices=ATTRIBUTES_CHOICES)

    def __str__(self):
        return self.name

class Trigger(models.Model):
    OPERATION_CHOICES = (
        ('lt','Less Than'),
        ('lte', 'Less Than Equal To'),
        ('eq', 'Equal To'),
        ('gte', 'Greater Than'),
        ('gt', 'Greater Than Equal To'),
    )
    name = models.CharField(max_length=50, default="None")
    signal_id = models.ForeignKey(Signal, on_delete=models.CASCADE)
    rules = models.ManyToManyField(Rule)
    operation = models.CharField(max_length=10, default='lt', choices=OPERATION_CHOICES)
    threshold_level = models.CharField(max_length=50)
    action_taken = models.ForeignKey(Action, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
