from django.contrib import admin

# Register your models here.
from todoapp.models import task

admin.site.register(task)
