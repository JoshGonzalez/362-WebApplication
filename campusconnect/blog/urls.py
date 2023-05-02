from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import RegisterView
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chat/', views.chat, name='chatroom'),
    path('profile/', views.profile, name='profile'),
    path('register/', RegisterView.as_view(), name='users-register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)