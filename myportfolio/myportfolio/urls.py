from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.portfolio, name='portfolio'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
