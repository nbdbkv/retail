from django.urls import path
from .views import StoreAPIView


urlpatterns = [
    path('', StoreAPIView.as_view()),
]
