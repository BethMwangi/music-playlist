# from django.shortcuts import render
from django.views.generic import TemplateView
from music.helpers import search_track, generate_play_list, get_random_string, get_lyrics
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def playlist_view(request, category):
    response  =  generate_play_list(category)
    return Response(response)
