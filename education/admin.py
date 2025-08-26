from django.contrib import admin
from . import models

# Register your models here.
#get all models from education app at the same time

for model in models.__all__:
    admin.site.register(model)


