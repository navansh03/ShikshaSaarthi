from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from . import views as resources_views


urlpatterns = [
    path('home/',resources_views.educational_content,name='educational_content'),

]



if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)