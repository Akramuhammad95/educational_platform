from django.contrib import admin

# Register your models here.

from .models import Users, Profile, activityLog
admin.site.register(Users)
admin.site.register(Profile)    
admin.site.register(activityLog)

