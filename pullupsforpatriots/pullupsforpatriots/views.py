import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Mail

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django import forms
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.utils.safestring import mark_safe

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your email'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Your message'})
    )

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = mark_safe("")
        self.fields['contact_email'].label = mark_safe("")
        self.fields['content'].label = mark_safe("")

def placeholder(request):
    return HttpResponse("Hello, world. This is a placeholder view.")
    
def ourcause(request):
    return render(request, 'ourcause.html')

def homepage(request):
    return render(request, 'homepage.html')

def moderncss(request):
    return render(request, 'modern-business.css', content_type='text/css')
    
def facss(request):
    return render(request, 'font-awesome.min.css', content_type='text/css')
    
def customcss(request):
    return render(request, 'custom.css', content_type='text/css')
    
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = Content('text/plain', template.render(context))

            #email = EmailMessage(
            #    "New contact form submission",
            #    content,
            #    "Your website" +'',
            #    ['youremail@gmail.com'],
            #    headers = {'Reply-To': contact_email }
            #)
            #email.send()
            print(content, contact_email)
            #send_mail("New contact form submission", content, "anguslmmclean@gmail.com", ['anguslmm@gmail.com'], fail_silently=False)
            sg = sendgrid.SendGridAPIClient(apikey='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')
            from_email = Email(contact_email)
            subject = "Contact Form message from PUfP"
            to_email = Email("anguslmm@gmail.com")
            mail = Mail(from_email, subject, to_email, content)
            response=sg.client.mail.send.post(request_body=mail.get())
            print("RESPONSE:" + str(response.status_code))
            print("done")
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })