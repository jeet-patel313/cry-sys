from django.contrib import admin

# Register your models here.
from .models import * #imports all the models

admin.site.register(Customer)
admin.site.register(Positiondata)