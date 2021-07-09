from django.urls import path

from .views import TenderSearchView, redirection_to_homepage, homepage, ProfileView
from django.urls import path, include

urlpatterns = [
    path('', redirection_to_homepage, name='redirection_to_homepage'),
    path('homepage/', homepage, name='homepage'),
    path('homepage/authentication/',
         include('django_registration.backends.activation.urls'),
         name='django_registration_register'),
    path('homepage/authentication/', include('django.contrib.auth.urls'), name='login'),
    path('homepage/search/', TenderSearchView.as_view(), name='tender_search'),
    path('profile/', ProfileView.as_view(), name='profile')
]