from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.album_list),
    path('midnights/', views.midnights_songs_list),
]
