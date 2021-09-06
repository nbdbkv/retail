from django.urls import path

from stores.views import StoreListView, StoreDetailView, buy, add

urlpatterns = [
    path('', StoreListView.as_view()),
    path('<int:pk>/', StoreDetailView.as_view()),
    path('<int:pk>/buy/', buy),
    path('<int:pk>/add/', add),
]
