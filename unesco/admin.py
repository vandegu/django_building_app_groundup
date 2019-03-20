from django.contrib import admin

# Register your models here.

from unesco.models import Site, Category, States, Region, Iso

admin.register(Site)
admin.register(Category)
admin.register(States)
admin.register(Region)
admin.register(Iso)
