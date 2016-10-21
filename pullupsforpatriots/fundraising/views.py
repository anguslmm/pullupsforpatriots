from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from django.template.loader import get_template

import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Mail

import urllib.request, urllib.parse

from .models import Marine, Sponsor, Donation, Pledge, Command

base_url = "http://www.pullupsforpatriots.com/donations/"


def placeholder(request):
    return HttpResponse("This is a placeholder.")


def companyd(request):
    marines = Marine.objects.filter(command=Command.objects.filter(name='Company D')[0]).order_by('-amount_raised')[:10]
    donations = Donation.objects.filter(marine__command=Command.objects.filter(name='Company D')[0], status="PAID")
    pledges = Pledge.objects.filter(marine__command=Command.objects.filter(name='Company D')[0], status="PAID")
    donation_goal = 10000.00
    donation_total = float(0)
    for donation in donations:
        donation_total += float(donation.amount)
    for pledge in pledges:
        donation_total += float(pledge.amount_paid)
    donation_progress = (donation_total / donation_goal) * 100
    form = SearchForm()
    return render(request, 'fundraising/companyd.html',
                  {'marines': marines, 'donation_total': donation_total, 'donation_progress': donation_progress,
                   'form': form})


def mcd(request):
    marines = Marine.objects.filter(command=Command.objects.filter(name='Marine Corps Detachment')[0]).order_by(
        '-amount_raised')[:10]
    donations = Donation.objects.filter(marine__command=Command.objects.filter(name='Marine Corps Detachment')[0],
                                        status="PAID")
    pledges = Pledge.objects.filter(marine__command=Command.objects.filter(name='Marine Corps Detachment')[0],
                                    status="PAID")
    donation_goal = 10000.00
    donation_total = float(0)
    for donation in donations:
        donation_total += float(donation.amount)
    for pledge in pledges:
        donation_total += float(pledge.amount_paid)
    donation_progress = (donation_total / donation_goal) * 100
    form = SearchForm()
    return render(request, 'fundraising/mcd.html',
                  {'marines': marines, 'donation_total': donation_total, 'donation_progress': donation_progress,
                   'form': form})


def af31st(request):
    marines = Marine.objects.filter(command=Command.objects.filter(name='31st IS')[0]).order_by('-amount_raised')[:10]
    donations = Donation.objects.filter(marine__command=Command.objects.filter(name='31st IS')[0], status="PAID")
    pledges = Pledge.objects.filter(marine__command=Command.objects.filter(name='31st IS')[0], status="PAID")
    donation_goal = 10000.00
    donation_total = float(0)
    for donation in donations:
        donation_total += float(donation.amount)
    for pledge in pledges:
        donation_total += float(pledge.amount_paid)
    donation_progress = (donation_total / donation_goal) * 100
    form = SearchForm()
    return render(request, 'fundraising/31stis.html',
                  {'marines': marines, 'donation_total': donation_total, 'donation_progress': donation_progress,
                   'form': form})


def af3rd(request):
    marines = Marine.objects.filter(command=Command.objects.filter(name='3rd IS')[0]).order_by('-amount_raised')[:10]
    donations = Donation.objects.filter(marine__command=Command.objects.filter(name='3rd IS')[0], status="PAID")
    pledges = Pledge.objects.filter(marine__command=Command.objects.filter(name='3rd IS')[0], status="PAID")
    donation_goal = 10000.00
    donation_total = float(0)
    for donation in donations:
        donation_total += float(donation.amount)
    for pledge in pledges:
        donation_total += float(pledge.amount_paid)
    donation_progress = (donation_total / donation_goal) * 100
    form = SearchForm()
    return render(request, 'fundraising/3rdis.html',
                  {'marines': marines, 'donation_total': donation_total, 'donation_progress': donation_progress,
                   'form': form})


def niocga(request):
    return render(request, 'fundraising/niocga.html')


def index(request):
    return render(request, 'fundraising/index.html')


def donate(request, marine_id):
    marine = get_object_or_404(Marine, pk=marine_id)
    form = DonateForm()
    return render(request, 'fundraising/donate.html', {'marine': marine, 'form': form})


def donation_start(request, marine_id):
    marine = get_object_or_404(Marine, pk=marine_id)
    try:
        params = {'METHOD': 'SetExpressCheckout',
                  'PAYMENTREQUEST_0_PAYMENTACTION': 'SALE',
                  'PAYMENTREQUEST_0_AMT': request.POST['amount'],
                  'PAYMENTREQUEST_0_CURRENCYCODE': 'USD',
                  'cancelUrl': 'http://www.google.com',
                  'returnUrl': base_url + 'donationconfirm/?marine_id=' + str(marine_id)}
        response = paypal_request(params)
        print(response)
        return redirect("https://www.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=" + response["TOKEN"])
    except:
        return redirect('donate', marine_id)


def pledge(request, marine_id):
    marine = get_object_or_404(Marine, pk=marine_id)
    form = PledgeForm()
    return render(request, 'fundraising/pledge.html', {'marine': marine, 'form': form})


def pledge_start(request, marine_id):
    marine = get_object_or_404(Marine, pk=marine_id)
    try:
        amount_per_pullup = float(request.POST['amount_per_pullup'])
        print(amount_per_pullup)
        if amount_per_pullup > 0:
            print("ok")
            params = {'METHOD': 'SetExpressCheckout',
                      'PAYMENTREQUEST_0_PAYMENTACTION': 'AUTHORIZATION',
                      'PAYMENTREQUEST_0_AMT': '0',
                      'PAYMENTREQUEST_0_CURRENCYCODE': 'USD',
                      'L_BILLINGTYPE0': 'MerchantInitiatedBillingSingleAgreement',
                      'L_BILLINGAGREEMENTDESCRIPTION0': 'PullUpsForPatriotsPledge',
                      'cancelUrl': 'http://www.google.com',
                      'returnUrl': base_url + 'pledgeconfirm/?marine_id=' + str(marine_id) + '&amount_per_pullup=' +
                                   request.POST['amount_per_pullup']}
            response = paypal_request(params)

            return redirect("https://www.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=" + response["TOKEN"])
        else:
            return redirect('pledge', marine_id)
    except:
        return redirect('pledge', marine_id)


def donation_confirm(request):
    marine = get_object_or_404(Marine, pk=int(request.GET.get('marine_id', '')))
    params = {
        'METHOD': 'GetExpressCheckoutDetails',
        'TOKEN': request.GET.get('token', '')}
    response = paypal_request(params)

    donation = Donation(
        marine=marine,
        amount=response['PAYMENTREQUEST_0_AMT'],
        donor_name=response['SHIPTONAME'],
        donor_email=response['EMAIL'],
        token=response['TOKEN'],
        payer_id=response['PAYERID'],
        correlation_id=response['CORRELATIONID'],
        status="INFO")

    marine.amount_raised = float(marine.amount_raised) + float(response['PAYMENTREQUEST_0_AMT'])

    donation.save()
    marine.save()

    return render(request, 'fundraising/donationconfirm.html', {'donation': donation
                                                                })


def pledge_confirm(request):
    marine = get_object_or_404(Marine, pk=int(request.GET.get('marine_id', '')))
    params = {
        'METHOD': 'GetExpressCheckoutDetails',
        'TOKEN': request.GET.get('token', '')}
    response = paypal_request(params)

    pledge = Pledge(
        marine=marine,
        amount_per_pullup=request.GET.get('amount_per_pullup', ''),
        donor_name=response['SHIPTONAME'],
        donor_email=response['EMAIL'],
        token=response['TOKEN'],
        payer_id=response['PAYERID'],
        correlation_id=response['CORRELATIONID'],
        status="INFO")

    pledge.save()

    return render(request, 'fundraising/pledgeconfirm.html', {'pledge': pledge
                                                              })


def donation_congrats(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id)

    params = {
        'METHOD': 'DoExpressCheckoutPayment',
        'TOKEN': donation.token,
        'PAYERID': donation.payer_id,
        'PAYMENTREQUEST_0_PAYMENTACTION': 'SALE',
        'PAYMENTREQUEST_0_AMT': donation.amount,
        'PAYMENTREQUEST_0_CURRENCYCODE': 'USD'
    }
    response = paypal_request(params)
    donation.status = 'PAID'
    donation.save()

    return render(request, 'fundraising/donationcongrats.html', {'donation': donation})


def pledge_congrats(request, pledge_id):
    pledge = get_object_or_404(Pledge, pk=pledge_id)

    params = {
        'METHOD': 'CreateBillingAgreement',
        'TOKEN': pledge.token
    }
    response = paypal_request(params)

    pledge.billing_agreement_id = response['BILLINGAGREEMENTID']
    pledge.save()

    return render(request, 'fundraising/pledgecongrats.html', {'pledge': pledge})


def sponsors(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'fundraising/sponsor_list.html', {'sponsors': sponsors})


def paypal_request(params):
    params.update({
        'USER': 'info_api1.pullupsforpatriots.com',
        'PWD': 'K3ZC4NESL9XFUYPE',
        'SIGNATURE': 'A1lRe-nNZspBh9GjWxQ8ua-eHAJJAtfY26Eq7lsS8ut1p6fB8us-HmFg',
        'VERSION': '86'})
    data = urllib.parse.urlencode(params).encode('ascii')

    with urllib.request.urlopen("https://api-3t.paypal.com/nvp", data) as f:
        # This line takes the response and turns it into a dictionary. It is magic, and I made it.
        # It is on one line because I am a fucking boss. If you can't read it, kiss my ass.
        # return_values = dict([[urllib.parse.unquote(a) for a in b] for b in [ a.split('=') for a in f.read().decode('utf-8').split('&')]])
        return_values = dict([[urllib.parse.unquote(name_or_value) for name_or_value in split_nvp] for split_nvp in
                              [unsplit_nvp.split('=') for unsplit_nvp in f.read().decode('utf-8').split('&')]])

    return return_values


def view_all(request, command_id):
    command = get_object_or_404(Command, pk=command_id)
    marine_list = Marine.objects.filter(command=command)
    sorted(marine_list, key=lambda a: a.get_last_name())
    paginator = Paginator(marine_list, 25)

    form = SearchForm()

    page = request.GET.get('page')
    try:
        marines = paginator.page(page)
    except PageNotAnInteger:
        marines = paginator.page(1)
    except EmptyPage:
        marines = paginator.page(paginator.num_pages)

    return render(request, 'fundraising/view_all.html', {'marines': marines, 'form': form, 'command': command})


def search(request):
    marines = Marine.objects.filter(name__icontains=request.GET.get('terms', ''))
    form = SearchForm()
    return render(request, 'fundraising/search.html', {'marines': marines, 'form': form})


def moderncss(request):
    return render(request, 'fundraising/modern-business.css', content_type='text/css')


def facss(request):
    return render(request, 'fundraising/font-awesome.min.css', content_type='text/css')


def customcss(request):
    return render(request, 'fundraising/custom.css', content_type='text/css')


class DonateForm(forms.Form):
    amount = forms.DecimalField(label="I would like to donate this much:", max_digits=9, decimal_places=2,
                                required=True)


class PledgeForm(forms.Form):
    amount_per_pullup = forms.DecimalField(label="I would like to donate this much per pull up:", max_digits=9,
                                           decimal_places=2, required=True)


class SearchForm(forms.Form):
    terms = forms.CharField(label="Search for service members by name:", required=True)


def send_confirm_email(pledge_id):
    the_pledge = Pledge.objects.get(id=pledge_id)
    template = get_template('fundraising/confirm_template.txt')
    context = {
        'donor': str(the_pledge.donor_name),
        'amount_per_pullup': str(the_pledge.amount_per_pullup),
        'marine_name': str(the_pledge.marine.name),
        'pullups': str(the_pledge.marine.pull_ups),
        'total': '%.2f' % (float(the_pledge.amount_per_pullup) * int(the_pledge.marine.pull_ups))
    }
    content = Content('text/plain', template.render(context))


    print(content, the_pledge.donor_email)
    sg = sendgrid.SendGridAPIClient(apikey=open('apikey.txt', 'r').read())
    from_email = Email("info@pullupsforpatriots.com")
    subject = "Thank you for your donation to Pull Ups for Patriots!"
    to_email = Email(str(the_pledge.donor_email))
    print(to_email)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print("RESPONSE:" + str(response.status_code))
    print("done")
