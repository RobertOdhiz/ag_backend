from django.contrib import admin
from django.urls import path, include
from users.views import ListUsers
from ghalas.views import GhalaSearchViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from feedback.views import FeedbackViewSet
from blog.views import BlogViewSet

router = DefaultRouter()
router.register(r'ghala', GhalaSearchViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'blog', BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListUsers.as_view(), name='list-users'),
    path('api/ghalas/', include('ghalas.urls')),
    path('api/', include(router.urls)),
    path('api/user/', include('users.urls')),
    path('api/myghalas/', include('myghala.urls')),
    path('api/sokos/', include('soko.urls')),
    path('api/profiles/', include('Profile.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)