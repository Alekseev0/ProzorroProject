from django.urls import path

from .views import TenderSearchView

urlpatterns = [
    path('', TenderSearchView.as_view(), name='tender_search'),
]