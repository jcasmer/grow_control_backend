"""grow_control_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from rest_framework.routers import DefaultRouter

from api import views as application_views

router = DefaultRouter()
router.register(r'user', application_views.user.UserViewSet)
router.register(r'user-full-data', application_views.user.UserFullDataViewSet, base_name='user_full_data')
router.register(r'type-diagnostic', application_views.type_diagnostic.TypeDiagnosticViewSet)
router.register(r'type-diagnostic-full-data', application_views.type_diagnostic.TypeDiagnosticFullDataViewSet, base_name='type_diagnostic_full_data')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', include('login.urls')) ,
    path('api/', include(router.urls)),
]
