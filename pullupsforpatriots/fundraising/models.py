from django.db import models

class Command(models.Model):
    name = models.CharField(max_length=200)
    personterm = models.CharField(max_length=200)
    personplural = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.name)

class Marine(models.Model):
    name = models.CharField(max_length=200)
    amount_raised = models.DecimalField('Amount Raised', max_digits=9, decimal_places=2, default=0)
    command = models.ForeignKey('Command',on_delete=models.CASCADE, default=0)
    pull_ups = models.PositiveSmallIntegerField(default=0)
    
    def get_last_name(self):
        if (len(str(self.name).split()) > 1):
            return str(self.name).split()[1][:-1]
        return str(self.name)

    def get_amount_per_pullup(self):
        return Pledge.objects.filter(marine__name=self.name).aggregate(models.Sum('amount_per_pullup'))
    
    def __str__(self):
        return str(self.name)
   
   
class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = models.URLField(max_length=200)
    site = models.URLField(max_length=200)
    description = models.TextField(max_length=2000)
    
    def __str__(self):
        return str(self.name)

class Donation(models.Model):
    marine = models.ForeignKey('Marine',on_delete=models.CASCADE)
    amount = models.DecimalField('Amount Donated', max_digits=9, decimal_places=2)
    donor_name = models.CharField(max_length=200)
    donor_email = models.EmailField()
    token = models.CharField(max_length=50)
    payer_id = models.CharField(max_length=50)
    correlation_id = models.CharField(max_length=50)
    status = models.CharField(max_length=10) # INIT, INFO, or PAID 
    
    def __str__(self):
        donation = str(self.amount) + ' to ' + str(self.marine)
        return donation


class Pledge(models.Model):
    marine = models.ForeignKey('Marine',on_delete=models.CASCADE)
    amount_per_pullup = models.DecimalField('Amount Pledged Per Pullup', max_digits=9, decimal_places=2)
    donor_name = models.CharField(max_length=200)
    donor_email = models.EmailField()
    token = models.CharField(max_length=50)
    payer_id = models.CharField(max_length=50)
    correlation_id = models.CharField(max_length=50)
    status = models.CharField(max_length=10) # INIT, INFO, or PAID
    billing_agreement_id = models.CharField(max_length=50)
    amount_paid = models.DecimalField('Amount Paid', max_digits=9, decimal_places=2, default=0)
    amount = models.DecimalField(decimal_places=2, max_digits=9, default=0) # this is a straight up bandaid. Sorry.
    
    def __str__(self):
        donation = str(self.amount_per_pullup) + ' for every pull up ' + str(self.marine) + 'does.'
        return donation

