from django.contrib import admin

# Register your models here.

from users.models import CustomUser, Profile

admin.site.register([CustomUser, Profile])
