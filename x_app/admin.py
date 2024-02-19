from django.contrib import admin

# Register your models here.
from x_app import models

admin.site.register(models.Login)
admin.site.register(models.Student)
admin.site.register(models.Admin1)
