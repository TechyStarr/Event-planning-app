from django.contrib import admin
from api.models import User, Event, Host, Guest


# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Host)
admin.site.register(Guest)

