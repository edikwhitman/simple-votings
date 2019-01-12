from django.contrib import admin
from .models import VoteModel, ReportModel


# Define the admin class
class VoteAdmin(admin.ModelAdmin):
    list_display = ('question', 'options')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('link', 'text', 'status', 'author')


# Register your models here.

admin.site.register(VoteModel, VoteAdmin)
admin.site.register(ReportModel, ReportAdmin)
