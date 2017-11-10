# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Accounts.models import UserProfile

# Register your models here.
from .models import Contractor,Client,Project,Task

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','title', 'email')
    search_fields = ('first_name', 'last_name','title')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','company', 'email')
    search_fields = ('first_name', 'last_name','company')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projectname', 'client','start_date')
    list_filter = ('start_date',)

class TaskAdmin(admin.ModelAdmin):
    list_display =('projectname','week','Task')
    list_filter =('projectname',)



admin.site.register(Project,ProjectAdmin)
admin.site.register(Contractor,ContractorAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(UserProfile)

admin.site.site_header = 'Salt Flats Admin'
admin.site.site_title = 'Dashboard'
admin.site.index_title = 'Admin Dashboard'
