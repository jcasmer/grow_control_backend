# pylint: disable=C0111
'''
'''
from django.urls import path, include

from .views import LoginView, LogoutView

urlpatterns = [ # pylint: disable=C0103
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]