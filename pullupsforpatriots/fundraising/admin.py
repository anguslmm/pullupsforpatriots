from django.contrib import admin

from .models import Marine, Command, Pledge, Donation, Sponsor

# Register your models here.
admin.site.register(Marine)
admin.site.register(Command)
admin.site.register(Sponsor)