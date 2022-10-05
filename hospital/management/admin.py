from django.contrib import admin

from management.views import billGenerator, invoice
from .models import billing, hospital,patient,doctor,comment,User
# Register your models here.

admin.site.register(hospital)
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(comment)
admin.site.register(User)
admin.site.register(billing)