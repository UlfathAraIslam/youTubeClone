from django.urls import path
from .views import ShortsView, ShortsWatchView

urlpatterns = [
    path('',ShortsView.as_view(), name='shorts'),
    path('watch/',ShortsWatchView.as_view(), name='watch')
]