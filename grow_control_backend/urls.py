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
router.register(r'group', application_views.groups.GroupsViewSet)
router.register(r'group-full-data', application_views.groups.GroupsFullDataViewSet, base_name='group_full_data')
router.register(r'type-diagnostic', application_views.type_diagnostic.TypeDiagnosticViewSet)
router.register(r'type-diagnostic-full-data', application_views.type_diagnostic.TypeDiagnosticFullDataViewSet, base_name='type_diagnostic_full_data')
router.register(r'advices', application_views.advices.AdvicesViewSet)
router.register(r'advices-full-data', application_views.advices.AdvicesFullDataViewSet, base_name='advices-full-data')
router.register(r'relationship', application_views.relationship.RelationshipViewSet)
router.register(r'relationship-full-data', application_views.relationship.RelationshipFullDataViewSet, base_name='relationship-full-data')
router.register(r'parents', application_views.parents.ParentsViewSet)
router.register(r'parents-full-data', application_views.parents.ParentsFullDataViewSet, base_name='parents-full-data')
router.register(r'childs', application_views.childs.ChildsViewSet)
router.register(r'childs-full-data', application_views.parents.ParentsFullDataViewSet, base_name='childs-full-data')
router.register(r'parents-childs', application_views.parents_childs.ParentsChildsViewSet)
router.register(r'parents-childs-full-data', application_views.parents_childs.ParentsChildsFullDataViewSet, base_name='parents-childs-full-data')
router.register(r'childs-detail', application_views.childs_detail.ChildsDetailViewSet)
router.register(r'childs-detail-full-data', application_views.childs_detail.ChildsDetailFullDataViewSet, base_name='childs-detail-full-data')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', include('login.urls')) ,
    path('api/', include(router.urls)),
    path('api/validate-parent/', application_views.validate_parents.ValidateParentsView),
    path('api/register-child/', application_views.register_child.RegistrationChildView),
    path('api/chart-child/', application_views.chart_child_data.ChartChildDataView),
    path('api/suggestions/', application_views.suggestions.SuggestionsView),
]
