from django.contrib import admin

from Account.models import User
from userprofile.models import MyProfile

admin.site.register(User)
admin.site.register(MyProfile)