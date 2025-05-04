from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from config.settings import DEBUG

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('catalog.urls')),
                  path('blogs/', include('blog.urls')),
                  path('mailing/', include('mailing.urls', namespace='mailing')),
    ]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)