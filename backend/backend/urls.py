from django.contrib import admin
from django.urls import path, include
from users.views import ListUsers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListUsers.as_view(), name='list-users'),
    path('api/ghala/', include('ghalas.urls')),
    path('api/user/', include('users.urls')),
    path('api/myproducts/', include('myghala.urls')),
]
