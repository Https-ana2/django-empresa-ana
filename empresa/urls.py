"""
URL configuration for empresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Importa as views de autenticação
from django.contrib.auth import views as auth_views 

urlpatterns = [
    # Mapeia a raiz (/) para a página de Login (NOVA LINHA)
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), 
    
    # URL de Logout (NOVA LINHA)
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    path('admin/', admin.site.urls),
    
    # Move a aplicação 'rh' para a rota '/app/'
    path('app/', include('rh.urls')),
    
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)