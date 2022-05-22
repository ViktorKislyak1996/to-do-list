from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from main import urls
from todo_list import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


