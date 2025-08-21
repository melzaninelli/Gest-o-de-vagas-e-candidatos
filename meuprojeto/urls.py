from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vagas/', include('vagas.urls')),
    path('candidatos/', include('candidatos.urls')),
    path('dashboard/', include('dashboard.urls')),
]
