from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from . import views as resources_views


urlpatterns = [
    path('educational_content/',resources_views.educational_content,name='educational_content'),
    path('course/<str:slug>/',resources_views.CourseOverview,name='coursepage'),

]



if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)