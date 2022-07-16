from django.contrib import admin
from .models import Person

# Register your models here.


# admin.site.register(Person)

@admin.register(Person)
class PersonModel(admin.ModelAdmin):
    list_filter = ('first_name','last_name')
    list_display = ('first_name','last_name')