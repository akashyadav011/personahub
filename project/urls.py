from django.contrib import admin
from django.urls import path, include

# 1️⃣ Correct import of the settings object
from django.conf import settings                                     # :contentReference[oaicite:1]{index=1}

# 2️⃣ Helper to serve static/media in DEBUG mode
from django.conf.urls.static import static                           # :contentReference[oaicite:2]{index=2}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls')),
]

# 3️⃣ Guard with DEBUG, not APPEND_SLASH
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
