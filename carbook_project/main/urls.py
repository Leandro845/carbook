from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('cars/', include('cars.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('payments/', include('payments.urls'))
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

