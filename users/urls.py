from django.urls import path
from . import views

urlpatterns = [
    path('petrol-spy/leaderboard/', views.user_pertol_spy_api_view),
]