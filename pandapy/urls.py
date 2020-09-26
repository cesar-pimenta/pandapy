
# servir media localmente
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from .view import hello_word

urlpatterns = [
    path('hello/', hello_word),
    path('admin/', admin.site.urls),
    path('blog/', include('web_site.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
