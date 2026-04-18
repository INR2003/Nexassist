from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
]

# Serve static files and images in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Serve frontend images
    urlpatterns += [
        # Serve frontend built JS/CSS assets
        re_path(r'^assets/(?P<path>.*)$', serve, {
            'document_root': settings.FRONTEND_DIR / 'assets',
        }),
        re_path(r'^images/(?P<path>.*)$', serve, {
            'document_root': settings.FRONTEND_DIR / 'images',
        }),
    ]

# Serve frontend - catch-all for React Router (must be last)
urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]