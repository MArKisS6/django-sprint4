from django.contrib import admin
from django.urls import include, path

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.custom_500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('', include('blog.urls')),
]
