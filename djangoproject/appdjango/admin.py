from django.contrib import admin

from appdjango.models import Person
# Create your models here.
@admin.register(Person)
class ShowId(admin.ModelAdmin):
    list_display = ('id', 'name','username','email','password','role' )
