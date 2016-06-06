from django.db import models

class Marines(models.Model):
    name = models.CharField(max_length=200)
    amount_raised = models.DecimalField('Amount Raised', max_digits=9, decimal_places=2)
    
class Donor(models.Model):
    name=models.CharField(max_length=200)
   
# Sponsor model goes here (replace this line with it).

class Donation(models.Model):
    marine = models.ForeignKey('Marines',on_delete=models.CASCADE)
    amount_donated = models.DecimalField('Amount Donated', max_digits=9, decimal_places=2)
    donor = models.ForeignKey('Donor', on_delete=models.CASCADE)
    message = models.TextField(max_length=200)
    public = models.BooleanField(Default=True)
    