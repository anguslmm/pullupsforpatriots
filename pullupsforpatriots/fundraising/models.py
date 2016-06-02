from django.db import models

class Marines(models.Model):
    name = models.CharField(max_length=200)
    amount_raised = models.DecimalField('Amount Raised', max_digits=9, decimal_places=2)

# Donor model goes here (replace this line with it).

# Sponsor model goes here (replace this line with it).

# Donation model goes here (replace this line with it).