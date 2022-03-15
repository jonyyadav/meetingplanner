from django.contrib import admin

# Register your models here.
from meeting.models import Meeting, Person, Room

admin.site.register(Room)
admin.site.register(Meeting)
admin.site.register(Person)