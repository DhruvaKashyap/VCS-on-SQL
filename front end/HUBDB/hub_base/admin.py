from django.contrib import admin
from .models import *
#from django.contrib.admin.models import LogEntry

#LogEntry.objects.all().delete()
# Register your models here.
admin.site.register(Coder)
admin.site.register(Commits)
admin.site.register(Repository)
admin.site.register(Employee)
admin.site.register(Extension)
admin.site.register(Files)
admin.site.register(Salary)
admin.site.register(Starred)
admin.site.register(Server)
