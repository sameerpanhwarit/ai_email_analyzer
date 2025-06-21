from django.urls import path
from .views import AnalyzeEmailView

urlpatterns = [
    path('analyze/', AnalyzeEmailView.as_view()),
]
