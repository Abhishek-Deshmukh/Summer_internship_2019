from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'institute', 'email' )
    list_per_page = 20
    search_field = ('name', )
    list_filter = ('institute', 'designation')

admin.site.register(Member, MemberAdmin)
admin.site.unregister(Group)
