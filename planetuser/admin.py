from planetuser.models import MyUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

admin.site.register(MyUser, UserAdmin)
