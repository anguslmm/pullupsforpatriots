from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic
from django.template import Context

import urllib.request, urllib.parse

from .models import Marine, Sponsor, Donation, Pledge

base_url = "https://pull-ups-for-patriots-anguslmm.c9users.io/donations/"

def placeholder(request):
    return HttpResponse("This is a placeholder.")
    
def companyd(request):
    return render(request, 'fundraising/companyd.html')
    
def niocga(request):
    return render(request, 'fundraising/niocga.html')
    
def index(request):
    return render(request, 'fundraising/index.html')
    
def donation_start(request, marine_id, amount):
    marine = get_object_or_404(Marine, pk=marine_id)
    params={'METHOD': 'SetExpressCheckout',
        'PAYMENTREQUEST_0_PAYMENTACTION':'SALE',
        'PAYMENTREQUEST_0_AMT':amount,
        'PAYMENTREQUEST_0_CURRENCYCODE':'USD',
        'cancelUrl':'http://www.google.com',
        'returnUrl': base_url + 'donationconfirm/?marine_id=' + str(marine_id)}
    response = paypal_request(params)
    return redirect("https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token="+response["TOKEN"])
    
def pledge_start(request, marine_id, amount_per_pullup):
    marine = get_object_or_404(Marine, pk=marine_id)
    params={'METHOD': 'SetExpressCheckout',
        'PAYMENTREQUEST_0_PAYMENTACTION':'AUTHORIZATION',
        'PAYMENTREQUEST_0_AMT':'0',
        'PAYMENTREQUEST_0_CURRENCYCODE':'USD',
        'L_BILLINGTYPE0':'MerchantInitiatedBillingSingleAgreement',
        'L_BILLINGAGREEMENTDESCRIPTION0':'PullUpsForPatriotsPledge',
        'cancelUrl':'http://www.google.com',
        'returnUrl': base_url + 'pledgeconfirm/?marine_id=' + str(marine_id) + '&amount_per_pullup=' + str(amount_per_pullup)}
    response = paypal_request(params)
    
    return redirect("https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token="+response["TOKEN"])
    
def donation_confirm(request):
    marine = get_object_or_404(Marine, pk=int(request.GET.get('marine_id', '')))
    params = {
        'METHOD': 'GetExpressCheckoutDetails',
        'TOKEN' : request.GET.get('token', '')}
    response = paypal_request(params)
    
    donation = Donation(
        service_member=marine,
        amount = response['PAYMENTREQUEST_0_AMT'],
        donor_name = response['SHIPTONAME'],
        donor_email = response['EMAIL'],
        token = response['TOKEN'],
        payer_id = response['PAYERID'],
        correlation_id = response['CORRELATIONID'],
        status = "INFO")
        
    donation.save()
    context = Context({'donation' : donation
    })
    
    return render(request, 'fundraising/donationconfirm.html', context)
    
def pledge_confirm(request):
    marine = get_object_or_404(Marine, pk=int(request.GET.get('marine_id', '')))
    params = {
        'METHOD': 'GetExpressCheckoutDetails',
        'TOKEN': request.GET.get('token', '')}
    response = paypal_request(params)
    
    pledge = Pledge(
        service_member=marine,
        amount_per_pullup = request.GET.get('amount_per_pullup', ''),
        donor_name = response['SHIPTONAME'],
        donor_email = response['EMAIL'],
        token = response['TOKEN'],
        payer_id = response['PAYERID'],
        correlation_id = response['CORRELATIONID'],
        status = "INFO")
        
    pledge.save()
    context = Context({'pledge' : pledge
    })
    
    return render(request, 'fundraising/pledgeconfirm.html', context)
    
def donation_congrats(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id)
    
    params = {
        'METHOD': 'DoExpressCheckoutPayment',
        'TOKEN' : donation.token,
        'PAYERID': donation.payer_id,
        'PAYMENTREQUEST_0_PAYMENTACTION' : 'SALE',
        'PAYMENTREQUEST_0_AMT' : donation.amount,
        'PAYMENTREQUEST_0_CURRENCYCODE' : 'USD'
    }
    response = paypal_request(params)
    donation.status = 'PAID'
    donation.save()
    context = Context({'donation' : donation})
    return render(request, 'fundraising/donationcongrats.html', context)
    
def pledge_congrats(request, pledge_id):
    pledge = get_object_or_404(Pledge, pk=pledge_id)
    
    params = {
        'METHOD': 'CreateBillingAgreement',
        'TOKEN': pledge.token
    }
    response = paypal_request(params)
    
    pledge.billing_agreement_id = response['BILLINGAGREEMENTID']
    pledge.save()
    context = Context({'pledge' : pledge})
    return render(request, 'fundraising/pledgecongrats.html', context)

class SponsorsView(generic.ListView):
    model = Sponsor
    template_name = 'sponsor_list.html'
    
def paypal_request(params):
    params.update({
        'USER': 'anguslmm_api1.gmail.com',
        'PWD':'TLEPFZQW4KAC3XTX',
        'SIGNATURE':'AxB4j059JJPICRcbFXrmLOtJzjWuAzJQj8.l1WxiSiz7cHqTjbSzhpYB',
        'VERSION':'86'})
    data = urllib.parse.urlencode(params).encode('ascii')
    
    with urllib.request.urlopen("https://api-3t.sandbox.paypal.com/nvp", data) as f:
        # This line takes the response and turns it into a dictionary. It is magic, and I made it.
        # It is on one line because I am a fucking boss. If you can't read it, kiss my ass.
        # return_values = dict([[urllib.parse.unquote(a) for a in b] for b in [ a.split('=') for a in f.read().decode('utf-8').split('&')]])
        return_values = dict([[urllib.parse.unquote(name_or_value) for name_or_value in split_nvp] for split_nvp in [ unsplit_nvp.split('=') for unsplit_nvp in f.read().decode('utf-8').split('&')]])
    
    
    return return_values
