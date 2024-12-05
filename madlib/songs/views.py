from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def album_list(request):
    return render(request, "album_list.html")


def midnights_songs_list(request):

    context = {
        "album_name": "Midnights",
        "song_titles": ["Lavender Haze", "Maroon", "Anti-Hero", "Snow On The Beach", "You're On Your Own, Kid"],
    }
    return render(request, "midnights_song_list.html", context)
