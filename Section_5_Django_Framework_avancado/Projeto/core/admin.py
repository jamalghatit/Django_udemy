from django.contrib import admin

from .models import Role, Service, Team
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('services', 'icon', 'active', 'modified')
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'active', 'modified')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'active', 'modified')