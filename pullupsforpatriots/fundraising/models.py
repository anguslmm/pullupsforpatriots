from django.db import models

class Marines(models.Model):
    marine_name = models.CharField(max_length=200)
    amount_raised = models.DecimalField('Amount Raised')

# Donor model goes here (replace this line with it).

# Sponsor model goes here (replace this line with it).

# Donation model goes here (replace this line with it).