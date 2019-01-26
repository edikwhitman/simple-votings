from django.contrib import admin
from .models import VoteModel, ReportModel, CheckedVoting


# Define the admin class
class VoteAdmin(admin.ModelAdmin):
    list_display = ('question', 'options')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('link', 'text', 'status', 'author')


class CheckedVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'voting_id')


# Register your models here.

admin.site.register(VoteModel, VoteAdmin)
admin.site.register(ReportModel, ReportAdmin)
admin.site.register(CheckedVoting, CheckedVoteAdmin)
