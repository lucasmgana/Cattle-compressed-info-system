from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wanyama/', include('wanyama.urls')),
    path('', include('farmer.urls')),
    path('', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
