from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('', admin.site.urls),
    path('auth/', include('server.auth_app.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('chat/', include('server.chats_app.urls'))
]
