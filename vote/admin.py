from django.contrib import admin
from .models import VoteModel


# Define the admin class
class VoteAdmin(admin.ModelAdmin):
    list_display = ('question', 'options')


# Register your models here.

admin.site.register(VoteModel, VoteAdmin)
