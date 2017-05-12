from django.db import models
from multiselectfield import MultiSelectField

class Action(models.Model):
    name = models.CharField(max_length=50, default="None")
    key = models.CharField(max_length=50, default="None")
    def __str__(self):
        return self.name

class Signal(models.Model):
    SERVICES_CHOICES = (
        ('identity','IDENTITY'),
        ('order', 'ORDER'),
    )
    ATTRIBUTES_CHOICES = (
        ('email','User Email'),
        ('cancelled_order', 'Cancelled Orders'),
        ('refund_order', 'Refund Orders'),
        ('order_count', 'Total Orders'),
        ('margin', 'Margin'),
    )
    name = models.CharField(max_length=50, default="None")
    services = models.CharField(max_length=10, default='identity', choices=SERVICES_CHOICES)
    attributes = MultiSelectField(default='email', choices=ATTRIBUTES_CHOICES)

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
    signals = models.ManyToManyField(Signal)
    operation = models.CharField(max_length=10, default='lt', choices=OPERATION_CHOICES)
    threshold_level = models.CharField(max_length=50)
    action_taken = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='triggers')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
