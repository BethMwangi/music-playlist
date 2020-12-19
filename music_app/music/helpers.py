import os
import requests
import json 
import random

from music_app.settings import  URL, API_KEY

url = URL


api_key = API_KEY

playlist = []

def search_track(q_track):
    """function that querys the track : track.search"""
    track = {}
    response = requests.get("{}/track.search?format=json&callback=json&q_lyrics={}&apikey={}".format(url, q_track, api_key))
    try:
        res = response.json()
        genre_list = res['message']['body']['track_list']
        if len(genre_list) > 0:
            track['track_id'] = genre_list[0]['track']['track_id']
            track['artist_name'] = genre_list[0]['track']['artist_name']
            track['has_lyrics'] = genre_list[0]['track']['has_lyrics']
            track['lyrics'] = get_lyrics(genre_list[0]['track']['track_id'])
        if track not in playlist:
            playlist.append(track)
        return track
    except  Exception as ex:
        print("seems there is an error", error=str(ex))
        return {}

def get_random_string(lyrics):
    lyrics_arr = lyrics.split()
    if len(lyrics_arr) >= 5:
        random_words = random.choices(lyrics_arr, k=5)
    else:
        return []
    return random_words

def get_lyrics(track_id):
    response = requests.get("{}/track.lyrics.get?format=json&callback=json&track_id={}&apikey={}".format(url, track_id, api_key))
    res = response.json()
    lyrics = ''
    if res['message']['header']['status_code'] == 200:
        lyrics = res['message']['body']['lyrics']['lyrics_body']
    return lyrics


def generate_play_list(category):
    track = search_track(category)
    if not track or track['has_lyrics'] == 0:
        print('this is plalist', playlist)
        return playlist
    random_words = " ".join(get_random_string(track['lyrics']))
    return generate_play_list(random_words)