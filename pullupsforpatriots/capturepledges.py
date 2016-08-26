from fundraising.models import Marine, Command, Pledge
from fundraising.views import paypal_request

for pledge in Pledge.objects.filter(status='INFO'):
    marine = pledge.service_member
    amount_to_capture = float(marine.pull_ups) * float(pledge.amount_per_pullup)
    try:
        print('Getting '+str(amount_to_capture)+' for '+str(marine.name))
        params = {
        'METHOD': 'DoReferenceTransaction',
        'REFERENCEID': str(pledge.billing_agreement_id),
        'AMT':str(amount_to_capture),
        'CURRENCYCODE':'USD',
        'PAYMENTACTION':'SALE',
        }
        response = paypal_request(params)
        print(response)
        pledge.amount_paid = amount_to_capture
        pledge.status = 'PAID'
        marine.amount_raised = float(marine.amount_raised) + float(response['AMT'])
        pledge.save()
        marine.save()
    except:
        print('Failed to capture' + str(amount_to_capture)+' for '+str(marine.name))