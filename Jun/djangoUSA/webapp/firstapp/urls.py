from django.urls import path
from.import views
urlpatterns = [
    path("", views.firstview),  # Include URLs from firstapp
    path("insert/", views.insertview),  # Include URLs from firstapp
    path("welcome/", views.welcomeview),  # Include URLs from firstapp
]
