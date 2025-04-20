from .models import SiteSettings

def site_settings(request):
    settings = SiteSettings.objects.first()
    return {
        'primary_color': settings.primary_color if settings else '#007bff',
        'secondary_color': settings.secondary_color if settings else '#6c757d',
        'resume_url': settings.resume.url if settings and settings.resume else None,
    }