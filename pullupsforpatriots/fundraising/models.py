from django.db import models

class Marines(models.Model):
    name = models.CharField(max_length=200)
    amount_raised = models.DecimalField('Amount Raised', max_digits=9, decimal_places=2)
    
class Donor(models.Model):
    name=models.CharField(max_length=200)
   
class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = models.URLField(max_length=200)
    site = models.URLField(max_length=200)
    description = models.TextField(max_length=200)

class Donation(models.Model):
    marine = models.ForeignKey('Marines',on_delete=models.CASCADE)
    amount = models.DecimalField('Amount Donated', max_digits=9, decimal_places=2)
    donor = models.ForeignKey('Donor', on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    public = models.BooleanField(Default=True)
    