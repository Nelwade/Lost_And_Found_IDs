from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path('upload/', views.upload_lost_id, name='upload_lost_id'),
    path('<int:pk>/', views.id_detail, name='id_detail'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
