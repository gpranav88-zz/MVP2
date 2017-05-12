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
        ('email_similarity','User Email Similarity'),
        ('cancelled_order', 'Cancelled Orders'),
        ('refund_order', 'Refund Orders'),
        ('order_count', 'Total Orders'),
        ('low_margin', 'Low Margin'),
        ('high_margin', 'High Margin'),
        ('amount', 'Amount'),
        ('amount_paid', 'Amount Paid'),
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
    threshold_level = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
