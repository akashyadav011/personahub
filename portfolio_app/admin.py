from django.contrib import admin
from .models import SiteSettings, Profile, Education, SoftSkill, TechSkill, Project, Certification

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('primary_color', 'secondary_color')
    fieldsets = (
        (None, {'fields': ('primary_color','secondary_color','resume')}),
    )

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(SoftSkill)
admin.site.register(TechSkill)
admin.site.register(Project)
admin.site.register(Certification)