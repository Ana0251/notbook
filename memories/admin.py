from django.contrib import admin
from .models import Memory, Profile, Tags, Interests
# Register your models here.
admin.site.register(Memory)
admin.site.register(Profile)
admin.site.register(Tags)
admin.site.register(Interests)