from django.urls import path
from .views import ThreadListView, ThreadDetailView

urlpatterns = [
  path('', ThreadListView.as_view()),
  path('<int:pk>/', ThreadDetailView.as_view())
]